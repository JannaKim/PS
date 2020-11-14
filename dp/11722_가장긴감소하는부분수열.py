N = int(input())
L = list(map(int,input().split()))
dp=[]
for i in range(N):
    dp.append(1)
    for j in range(i):
        if L[j]>L[i] and dp[i]<dp[j]+1:
            dp[i]=dp[j]+1
print(max(dp))