import sys; input= lambda: sys.stdin.readline().rstrip()
n= int(input())
m= int(input())
dp= [[1e9]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a, b, c= map(int ,input().split())
    dp[a][b]= min(dp[a][b], c)

for i in range(1, n+1): # 중간에 이 간선 끼워넣음
    dp[i][i]=0
    for j in range(1, n+1):
        for k in range(1, n+1):
            dp[j][k]= min(dp[j][k], dp[j][i]+dp[i][k])
for i in range(1, n+1): # 중간에 이 간선 끼워넣음
    for j in range(1, n+1):
        print([dp[i][j], 0][dp[i][j]==1e9], end=' ')
    print()