n=int(input())
P=[*map(int, input().split())]
dp= [1] * n

for i in range (1,n):
    # dp[i] 계산
    for j in range (i):
        if P[j] < P[i]:
            dp[i] = max(dp[i], 1 + dp[j])

print(max(dp))


