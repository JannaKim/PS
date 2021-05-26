from itertools import combinations as combi 
n, m= map(int, input().split())
rate=[[*map(int, input().split())] for _ in range(n)]

L= list(range(m))
ans=-1
for ls in combi(L,3):
    tmp=0
    for i in range(n):
        tmp+=max([rate[i][el] for el in ls])
    ans=max(ans,tmp)
print(ans)

