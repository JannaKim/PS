'''
5 2

5!/(2!3!) = 10

'''
N, K = [int(i) for i in input().split()]

dp=[0]
for i in range(1,N+1):
    dp.append([0]*(i+1))
    dp[i][0]=1
    dp[i][-1]=1


for i in range(2,N+1):
    for j in range(1,len(dp[i])-1):
        dp[i][j] = (dp[i-1][j-1]+dp[i-1][j])%10007
        # dp[2][1] = dp[1][0]+dp[1][1]


print(dp[N][K])
