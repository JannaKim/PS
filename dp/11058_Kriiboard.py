n= int(input())
dp= [0]*(max(n,5)+1)

dp[1]= 1
dp[2]= 2
dp[3]= 3
dp[4]= 4
dp[5]= 5

if n<=5:
    print(dp[n])
    exit()

for i in range(6,n+1):
    dp[i]=max(dp[i-5]*4, dp[i-4]*3, dp[i-3] * 2)
print(dp[n])