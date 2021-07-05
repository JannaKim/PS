c, n = map(int, input().split())
pair = []
for _ in range(n):
    a, b = map(int, input().split())
    pair.append( (b, a))

dp = [1e9] * (c + 101)
for a, b in pair:
    for i in range(c + 1):
        if not i:
            dp[a] = min(dp[a], b)
        elif dp[i] != 1e9:
            dp[i + a] = min(dp[i + a], dp[i] + b)

print(min(dp[c:]))
