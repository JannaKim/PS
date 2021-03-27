n, k= map(int, input().split())
unit= []
for _ in range(n):
    unit.append(int(input()))

dp=[0]+ [1e9]*k
for coin in unit:
    for i in range(k+1):
        if not i or dp[i]:
            if i+coin<=k:
                dp[i+coin]= min(dp[i]+1, dp[i+coin])

print([dp[k],-1][dp[k]==1e9])