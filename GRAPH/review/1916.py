import sys; input= lambda: sys.stdin.readline().rstrip()
from heapq import heappop, heappush
n= int(input())
m= int(input())
edge= [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c= map(int, input().split())
    edge[a].append((b,c))

st, ed= map(int, input().split())
accum= [1e9 for _ in range(n+1)]
accum[st]=0
q=[]
heappush(q,(st, 0))
while q:
    v, cost= heappop(q)
    if accum[v]<cost:
        continue
    for v2, c in edge[v]:
        if cost+c<accum[v2]:
            accum[v2]= cost+c
            heappush(q, (v2, accum[v2]))
print(accum[ed])





