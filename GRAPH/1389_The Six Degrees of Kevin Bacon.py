n, m= map(int, input().split())
dp= [[1e9]*n for _ in range(n)]
for _ in range(m):
    a, b= [int(i)-1 for i in input().split()]
    dp[a][b]=1
    dp[b][a]=1

for i in range(n):
    dp[i][i]=0
    for j in range(n):
        for k in range(n):
            dp[j][k]= min(dp[j][k], dp[j][i]+ dp[i][k])

mn= 1e9
ans=-1
for i in range(n):
    cur= sum(dp[i])
    if cur < mn:
        mn= cur
        ans= i+1
print(ans)