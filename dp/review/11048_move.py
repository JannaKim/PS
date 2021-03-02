import sys; input= lambda: sys.stdin.readline().rstrip();r=range
n, m= map(int, input().split())
dp=[0]*(m+1)
for _ in r(1,n+1):
    cur=[*map(int, input().split())]
    for i in r(1,m+1):
        dp[i]= max(dp[i],dp[i-1])+cur[i-1]
print(dp[m])
