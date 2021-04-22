import sys; input= lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(1000000)
from heapq import heappop, heappush
n= int(input())
edge= [[] for _ in range(n+1)]
indegree= [[0,i] for i in range(n+1)]
for _ in range(n-1):
    u, v= map(int, input().split())
    edge[u].append(v)
    edge[v].append(u)
    indegree[u][0]-=1
    indegree[v][0]-=1
q=[]
[heappush(q,indegree[i]) for i in range(1,n+1)]
cnt=0
while q:
    deg, v= heappop(q)
    if indegree[v][0]!=deg:
        heappush(q,indegree[v])
        continue
    if not deg:break
    cnt+=1
    for v2 in edge[v]:
        indegree[v2][0]+=1

print(cnt)