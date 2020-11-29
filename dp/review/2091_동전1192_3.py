X, *nums= map(int, input().split())
units=[1,5,10,25]
dp= [[0]*5 for _ in range(X+1)]
'''
for i, unit in enumerate(units):
    for num in range(1,nums[i]+1):
        if unit*num<=X:
            if dp[unit*num][4]<num:
                dp[unit*num][4]= num
                dp[unit*num][i]= num

[print(i) for i in dp]
# 동전 하나로 채우는 경우 따로 빼면, 
# 같은 동전 i개가 이미 들어있을경우 같은 동전j개를 넣어서 x원을 만들어 버린다
'''
for i, unit in enumerate(units):
    for j in range(X-1,-1,-1):
        if dp[j][4] or j==0:
            for num in range(1,nums[i]+1):
                if j+unit*num<=X:
                    if dp[j+unit*num][4]<dp[j][4]+num:
                        dp[j+unit*num][4]=dp[j][4]+num
                        for k in range(4):
                            dp[j+unit*num][k]= dp[j][k]
                        dp[j+unit*num][i] +=num
                else:
                    break

print(*dp[X][:4])

