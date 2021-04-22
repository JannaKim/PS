n, k= map(int, input().split())
dp=[0]*(n+1)
L=[*map(int, input().split())]
for i in range(1,n+1):
    dp[i]=dp[i-1]+L[i-1]
ans=-100*100000-1
for i in range(k,n+1):
    ans=max(ans, dp[i]-dp[i-k])
print(ans)
'''
10 2
3 -2 -4 -9 0 3 7 13 8 -3
'''