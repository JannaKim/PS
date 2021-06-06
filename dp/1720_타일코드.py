n = int(input())
ln = max(2 , n)
dp = [0] * (ln + 1)
dp[1] = 1
dp[2] = 3
for i in range(3 , n + 1):
    dp[i] = dp[i - 2] * 2 + dp[i - 1]
if n <=2:
    print(dp[n])
elif n%2:
    print(dp[n] - (dp[n] - dp[n//2] )//2 )
else:
    print(dp[n] - (dp[n] - 2 * dp[n//2-1] - dp[n//2])//2)
