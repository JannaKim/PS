n = int(input())
dp = []
for i in range(n):
    dp.append([*map(int, input().split())])
    for j in range(n):
        if not dp[i][j]:
            dp[i][j] = 1e9


for i in range(n):
    for j in range(n):
        for k in range(n):
            dp[j][k] = min(dp[j][k], dp[j][i] + dp[i][k])


for i in range(n):
    for j in range(n):
        print([1, 0][dp[i][j] == 1e9], end = ' ')
    print()