n = int(input())

v, v2 = map(int, input().split())
m  = int(input())

dp = [[1e9]*(n + 1) for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    dp[a][b] = 1
    dp[b][a] = 1


for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, n + 1):
            dp[j][k] = min(dp[j][k], dp[j][i] + dp[i][k])

print([dp[v][v2], -1][dp[v][v2] == 1e9])