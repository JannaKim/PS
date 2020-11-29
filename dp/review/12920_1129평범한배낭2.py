N, M = map(int, input().split())
w, v, nums=[0]*N,[0]*N,[0]*N
for i in range(N):
    w[i], v[i], nums[i] = map(int, input().split())

dp = [0]*(M+1)
for i, wei in enumerate(w):
    for j in reversed(range(M+1)):
        if dp[j] or j==0:
            for num in range(1,nums[i]+1):
                if j+wei*num<=M:
                    if dp[j+wei*num]<dp[j]+v[i]*num:
                        dp[j+wei*num] = dp[j]+v[i]*num

print(max(dp))
'''
2 3
2 7 1
1 9 3
'''               


