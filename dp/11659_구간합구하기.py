import sys; input= lambda: sys.stdin.readline().rstrip()
n, m= map(int, input().split())
dp=[0]*(n+1)
L= [0]+[*map(int, input().split())]
dp[0]=0
for i in range(1,n+1):
    dp[i]=dp[i-1]+L[i]

for _ in range(m):
    a, b= map(int, input().split())
    print(dp[b]-dp[a-1])