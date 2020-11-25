from functools import cmp_to_key as cmp
K = int(input()) # 가방크기
n = int(input()) # 물건 개수
w = [int(i) for i in input().split()] # 무게
v = [int(i) for i in input().split()] # 가치

pf = [] # (가성비, 인덱스) cost performance

for i in range(n):
    if v[i]>=w[i]: # 가성비 1 이상
        pf.append((round(v[i]/w[i],2), i)) 
    else:
        pf.append((0, i))
pf.sort(key = cmp(lambda a, b: w[b[1]]-w[a[1]] if b[0]==a[0] else a[0]-b[0]), reverse=True) # 가성비 같으면 무게 작은것부터 넣는다.

print(pf)
MP = -1 # 노드 i까지 봤을 때 얻은 이익중 최댓값


def frac_knapsack(idx, size): # 가성비 이익 return
    #print('fk', idx, size)
    frac_sum = 0
    i = 0
    s = size
    #print(pf)
    while s>=0:
        while i<n and pf[i][1]<idx:
            i+=1
        # 남은 최고 가성비 인덱스: pf[i][1]
        #print(f'남은 최고 가성비 인덱스: {i}, {s}')
        if i>=n:
            return frac_sum
        if w[pf[i][1]]<=s:
            frac_sum+=v[pf[i][1]]
            s-=w[pf[i][1]]
            i+=1
        else:
            frac_sum+=s*pf[i][0] # 가성비 채워넣기
            i+=1
            return frac_sum
    return frac_sum

x = [-1]*n
def backtrack(i, size):
    global MP
    if i>=n or size <=0:
         # x: 점검하는 한계 함수(bounding function)
        return
    else:

        p = sum([v[j] if x[j]==1 else 0 for j in range(i) ]) # 골라진 애들 가치합


        # x[info] =1 을 따라가야 하는지 결정
        if w[i] <= size:
            B = frac_knapsack(i+1, size-w[i])

            if p+ v[i] + B> MP: # 그리디 상으로 가능성 o
                #print(i,'넣음',p+ v[i] + B, '>', MP)
                MP= max(MP,p+v[i])
                x[i]=1
                #print(x[:i+1], i, size)
                backtrack(i+1, size-w[i])
        # x[info] =0 을 따라가야 하는지 결정

        B = frac_knapsack(i+1, size)

        if p + B > MP:
            #print(i,'안넣음',p + B, '>', MP)
            x[i]= 0
            #print(x[:i+1], i, size)
            backtrack(i+1, size)
        

			

backtrack(0,K)

print(MP)
'''
7
4
6 4 1 3
13 8 0 6
'''