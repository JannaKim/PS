from collections import deque
n, m, v = map(int, input().split())

edge = [ [] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    edge[a].append(b)
    edge[b].append(a)

vis = [False] * (n + 1)
vis[v] = True
stc1 = []
def dfs(v):
    edge[v].sort()
    for v2 in edge[v]:
        if not vis[v2]:
            stc1.append(v2)
            vis[v2] = True
            dfs(v2)

stc1.append(v)
dfs(v)
print(*stc1)

vis = [False] * (n + 1)
vis[v] = True

stc2 = []

def bfs(st):
    q = deque()
    q.append(st)
    stc2.append(st)
    while q:
        v = q.popleft()
        edge[v].sort()
        for v2 in edge[v]:
            if not vis[v2]:
                stc2.append(v2)
                vis[v2] = True
                q.append(v2)
bfs(v)
print(*stc2)