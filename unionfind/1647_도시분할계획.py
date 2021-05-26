import sys; input= lambda: sys.stdin.readline().rstrip()
from heapq import heappush, heappop
n, m= map(int, input().split())
par= list(range(n+1))

def find(v):
    if par[v]==v:
        return v
    else:
        par[v]= find(par[v])
        return par[v]

def union(u, v):
    r1= find(u)
    r2= find(v)
    if r1<r2:
        par[r2]=r1
    else:
        par[r1]=r2
q=[]
for _ in range(m):
    a, b, c= map(int, input().split())
    heappush(q, (c,a,b))

ans=0
mx=0
while q:
    c,a,b= heappop(q)
    find(a)
    find(b)
    if par[a]!=par[b]:
        mx= max(mx,c)
        ans+=c
        union(a,b)
print(ans-mx)