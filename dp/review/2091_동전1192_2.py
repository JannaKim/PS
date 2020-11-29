X, *nums = map(int, input().split())
units=[1,5,10,25]

dp= [[0]*5 for _ in range(X+1)]
for i, unit in enumerate(units):
    for j in reversed(range(X+1)): # X~0원 순인 이유?
        if dp[j][4] or j==0:
            for num in range(1,nums[i]+1):
                if j+unit*num<=X:
                    if dp[j+unit*num][4]<dp[j][4]+num:
                        dp[j+unit*num][4] = dp[j][4]+num
                        for k in range(4):
                            dp[j+unit*num][k]=dp[j][k]
                        dp[j+unit*num][i]+=num
                else:
                    break

print(dp[X][:4])


