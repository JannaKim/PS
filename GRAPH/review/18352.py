import sys; input= lambda: sys.stdin.readline().rstrip()
from heapq import heappop, heappush
n, m, k, x= map(int, input().split())
edge= [[] for _ in range(n+1)]
for _ in range(m):
    a, b= map(int, input().split())
    edge[a].append(b)

q=[]
accum= [1e9]*(n+1)
accum[x]=0
heappush(q,(x,0))
while q:
    v,cst = heappop(q)
    if accum[v]<cst:
        continue
    for v2 in edge[v]:
        if cst+1<accum[v2]:
            accum[v2]= cst+1
            heappush(q, (v2,accum[v2]))
flag=False
for i in range(1,n+1):
    if accum[i]==k:
        flag=True
        print(i)
if not flag:
    print(-1)
