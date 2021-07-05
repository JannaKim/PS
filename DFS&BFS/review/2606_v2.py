n = int(input())
m = int(input())
edge = [ [] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    edge[a].append(b)
    edge[b].append(a)

vis = [False] *  (n + 1)
def dfs(v):
    for v2 in edge[v]:
        if not vis[v2]:
            vis[v2] = True
            dfs(v2)
vis[1] = True
dfs(1)
ans = 0
for i in range(2, n + 1):
    if vis[i]:
        ans += 1
print(ans)