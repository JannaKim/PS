'''
30만*30만 = 900억 = 90초   ∴ O(n^2) 일 때 TLE
nlogn = 545만
'''

N,A,B=[int(i) for i in input().split()]
A_based=[]
B_based=[]
I=[]
valid_striker=0
for i in range(N):
    a=list(map(int,input().split()))
    #AI.append((I[0]-A,I[1])) # 벡터를 튜플로 저장
    #BI.append((I[0]-B,I[1]))
    I.append((I[0],I[1])) # 좌표를 튜플로 저장


''' 어떻게?
실제로는 ccw 알고리즘을 인자로 주면 내부에서 그 알고리즘을 기준으로 정렬해줘요??
heap 이용?
min lambda
quick O^n?
'''


'''
AI.sort(key= lambda x: x[1]/x[0] ) # 기울기 작은 순으로 정렬
BI.sort(key= lambda x: x[1]/x[0] )
'''
def ccw_merge(loc, first, last, O):
    m = (first+last)//2
    i, j = first, m+1 # 앞쪽 반과 뒷쪽 반이 각각 ccw되어있다.
    B = []
    while i<=m and j<=last: #index안삐져나가게
        if (loc[i][0]-O)*loc[j][1] - loc[i][1]*(loc[j][0]-A) >= 0: #점i보다 점j가 왼쪽에있다
            B.append(loc[i])
            i+=1
        else:
            B.append(loc[j])
            j+=1
    if j>last: # 오른쪽 리스트가 다 사용됐다 = 왼쪽 리스트 잔여물 (o)
        B=B+loc[i:m+1]
    else: # if i>m
        B=B+loc[j:last+1]

    if O==A: #다른 거 그대로, 부분만 바뀌게 저장
        for i in range(first,last+1):
            A_based[i] = B[i-first]
    else: 
        for i in range(first,last+1):
            B_based[i] = B[i-first]

    
def divide_and_conquer(vec, first, last, O):
    if first >= last: return # 크기 1로 다 쪼갬
    divide_and_conquer(vec, first, (first+last)//2, O)
    divide_and_conquer(vec, (first+last)//2+1, last, O)
    ccw_merge(vec, first, last, O) # 각각 ccw된 두 리스트 merge


divide_and_conquer(I, 0, N-1, A)
divide_and_conquer(I, 0, N-1, B)



for i in range(len(B_based)): # B 등수 넣어주기
    A_based[A_based.index(B_based[i])] = (B_based[i], i)

for i in range(len(A_based)): # 기준 작은 기울기부터 유효공격수인지 검사
    # 지금 검사하는 애가 B기준 몇등?
    B_based_ranking = A_based[i][1]
    min_rank = min(key = lambda x:x[1], A_based[:i])  # 얘중에 B기준 가장 앞에 등수 찾는법 ??
    if min_rank[1]>B_based_ranking:
        valid_striker+=1

print(valid_striker)
