import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)


def dfs(nd):
    if dp[nd] != -1:
        return dp[nd]
    res = max((dfs(v) for v in tr[nd]), default=0) + d[nd]
    dp[nd] = res
    return res


for __ in range(int(input())):
    n, k = map(int, input().split())
    d = list(map(int, input().split()))
    tr = [[] for __ in range(n)]
    dp = [-1] * n
    for __ in range(k):
        x, y = map(int, input().split())
        x -= 1
        y -= 1
        tr[y].append(x)
    w = int(input())
    w -= 1
    print(dfs(w))
