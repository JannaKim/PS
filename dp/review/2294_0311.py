n, k= map(int, input().split())
unit= [int(input()) for _ in range(n)]

dp=[1]+[0]*k
for coin in unit:
    for i in range(k+1):
        if i+coin<=k:
            dp[i+coin]+=dp[i]

print([dp[k],-1][dp[k]==1e9])