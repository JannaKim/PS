n, k = map(int, input().split())
won = []
for _ in range(n):
    won.append(int(input()))

dp = [1]+[0]*k
for i in won:
    for j in range(1,k+1):
        if i<=j:
            dp[j]+=dp[j-i]
print(dp[k])

