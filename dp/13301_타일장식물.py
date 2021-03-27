n=int(input())
dp= [0]*(n+1)
dp[0]=1
dp[1]=1
if n==1:
    print(4)
    exit()
for i in range(2,n):
    dp[i]=dp[i-1]+dp[i-2]
print(2*dp[n-2]+4*dp[n-1])