a= input()
b= input()
n= len(a)
m= len(b)
dp= [[0]*(n+1) for _ in range(m+1)]

for i in range(m):
    for j in range(n):
        if b[i]==a[j]:
            dp[i+1][j+1]=1

for i in range(1,m+1):
    for j in range(1,n+1):
        if dp[i][j]:
            dp[i][j]=dp[i-1][j-1]+1
        else:
            dp[i][j]=max(dp[i-1][j], dp[i][j-1])

print(dp[m][n])