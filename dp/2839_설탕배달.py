n = int(input())
dp = [0] + [1e9] * n
for bag in (3 , 5):
    for i in range(n + 1):
        if not i or dp[i]:
            if i + bag <= n:
                dp[i + bag] = min(dp[i + bag] , dp[i] + 1)
    
print([dp[n] , -1][dp[n] == 1e9])