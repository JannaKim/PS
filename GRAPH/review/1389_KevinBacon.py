from collections import deque
n, m = map(int, input().split())
edge = [ [] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    edge[a].append(b)
    edge[b].append(a)


def bacon(v):
    q = deque()
    q.append((v, 0))
    ans = 0
    vis = [False] * (n + 1)
    vis[v] = True
    while q:
        v, lev = q.popleft()
        for v2 in edge[v]:
            if not vis[v2]:
                vis[v2] = True
                ans += lev + 1
                q.append((v2, lev + 1))
    return ans

winner = -1
mn = 1e9
for i in range(1, n + 1):
    tmp = bacon(i)
    if tmp < mn:
        mn = tmp
        winner = i
print(winner)