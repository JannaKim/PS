n=int(input())
if n==1:
    print(2)
    exit()
b=[0]*(n+1)
b[0]=0
b[1]=2
dp=[0]*(n+1)
dp[0]=0
dp[1]=2
dp[2]=7
b[2]=b[1]+2 * dp[1]
for i in range(3,n+1):
    b[i-1] = (2 * dp[i-2] + b[i-2]) % 1000000007
    dp[i] = (dp[i-2] + 2 * dp[i-1] + b[i-1]) % 1000000007
#print(b) 
    
print(dp[n])
