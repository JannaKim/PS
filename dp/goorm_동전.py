import math
K = 372
dp=[0]+[math.inf]*K
for won in [1,10,50,100]:
    for j in range(won,K+1):
        dp[j] = min(dp[j-won]+1, dp[j])

print(dp[K])