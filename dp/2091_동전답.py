dp=[[[0] for _ in range(5)] for __ in range(10000)]
a=[0,1,5,10,25]

X, *data = [int(i) for i in input().split()]
data.insert(0,0)

for i in range(1,5):
    for j in range(X,-1,-1):
        if dp[j][0] or j==0:
            for k in range(1,data[i]+1):
                if j+a[i]*k <=X and dp[j][0]+k>dp[j+a[i]*k][0]:
                    dp[j+a[i]*k][0] = dp[j][0]+k
                    for l in range(1,5):
                        dp[j+a[i]*k][l] = dp[j][l]
                    dp[j+a[i]*k][i] = dp[j][i]+l
print(*dp[X])
