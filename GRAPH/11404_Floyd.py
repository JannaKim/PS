import sys; input= lambda:sys.stdin.readline().rstrip()
n= int(input())
m= int(input())

dp= [ [1e9]*(n+1) for _ in range(n+1)]

for _  in range(m):
    a, b, c= map(int,input().split())
    if dp[a][b]>c:
        dp[a][b]=c



for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i!=j and dp[i][j]>dp[i][k]+dp[k][j]:
                dp[i][j]= dp[i][k]+dp[k][j]

for el in dp:
    for i in el[1:]:
        print([i,0][i==1e9], end=' ')
    print()