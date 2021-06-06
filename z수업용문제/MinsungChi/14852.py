n=int(input())
if n==1:
    print(2)
    exit()
b=[0]*(n+1)
b[0]=2
b[1]=6
dp=[0]*(n+1)
dp[0]=0
dp[1]=2
dp[2]=7
b[2]=b[1]+dp[2]*2
for i in range(3,n+1):
    
print(dp[n])
