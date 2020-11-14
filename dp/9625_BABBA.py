K= int(input())

dp=[1,0]
for _ in range(K):
    dp= [dp[1],dp[0]+dp[1]]

print(*dp)