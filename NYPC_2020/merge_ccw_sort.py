'''
5
2 6
4 5
5 7
6 6
7 9
'''

N = int(input())
vec = []
for i in range(N):
    vect = [int(i) for i in input().split()]
    vec.append((vect[0],vect[1]))


def ccw_merge(vec, first, last):
    m = (first+last)//2
    i, j = first, m+1 # 앞쪽 반과 뒷쪽 반이 각각 ccw되어있다.
    B = []
    while i<=m and j<=last: #index안삐져나가게
        if vec[i][0]*vec[j][1] - vec[i][1]*vec[j][0] >= 0: #점i보다 점j가 왼쪽에있다
            B.append(vec[i])
            i+=1
        else:
            B.append(vec[j])
            j+=1
    if j>last: # 오른쪽 리스트가 다 사용됐다 = 왼쪽 리스트 잔여물 o
        B=B+vec[i:m+1]
    else: # if i>m
        B=B+vec[j:last+1]
    for i in range(first,last+1): #??????????????????????
        vec[i] = B[i-first]

    
def divide_and_conquer(vec, first, last):
    if first >= last: return # 크기 1로 다 쪼갬
    divide_and_conquer(vec, first, (first+last)//2)
    divide_and_conquer(vec, (first+last)//2+1, last)
    ccw_merge(vec, first, last) # 각각 ccw된 두 리스트 merge

divide_and_conquer(vec,0, N-1)

print(vec)


