n= int(input())
L= [float(input()) for _ in range(n)]
dp=[1]*n
dp[0]=L[0]
for i in range(1,n):
    dp[i]= max(L[i],L[i]*dp[i-1])

print("%0.3f"%max(dp))
