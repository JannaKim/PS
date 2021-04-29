n, m, k= map(int, input().split())
y=n-1
x=m-1
if k:
    y=(k-1)//m
    x=(k-1)%m

dp= [[0]*m for _ in range(n)]
for i in range(y+1):
    for j in range(x+1):
        if 0<=i-1 and 0<=j-1:
            dp[i][j]= dp[i-1][j]+dp[i][j-1]
        else:
            dp[i][j]=1

for i in range(y,n):
    for j in range(x,m):
        if 0<=i-1 and 0<=j-1:
            dp[i][j]= dp[i-1][j]+dp[i][j-1]
        else:
            dp[i][j]=1
#[print(*el) for el in dp]
print(dp[n-1][m-1])

