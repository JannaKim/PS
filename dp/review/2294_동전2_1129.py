n, k = map(int, input().split())
unit=[]
for _ in range(n):
    unit.append(int(input()))

dp=[0]+[k+1]*(k)
for i in range(n):
    for j in range(unit[i],k+1):
        dp[j]=min(dp[j], dp[j-unit[i]]+1)
if dp[k]<=k:
    print(dp[k])
else:
    print(-1)