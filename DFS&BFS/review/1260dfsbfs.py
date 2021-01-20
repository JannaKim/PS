n, m, start= map(int, input().split())
edge= [[] for _ in range(n+1)]
import sys; sys.setrecursionlimit(10000)
from collections import deque

for _ in range(m):
    a, b= map(int, input().split())
    edge[a].append(b)
    edge[b].append(a)

for i in range(1,n+1):
    edge[i].sort()

visited= [False for _ in range(n+1)]
def dfs(v):
    visited[v]=True
    print(v,end=' ')

    for v2 in edge[v]:
        if not visited[v2]:
            dfs(v2)

dfs(start)
print()
D = deque()
D.append(start)
print(start, end=' ')
visited= [False for _ in range(n+1)]
visited[start]=True
while D:
    v= D.popleft()

    for v2 in edge[v]:
        if not visited[v2]:
            visited[v2]=True
            print(v2, end=' ')
            D.append(v2)
