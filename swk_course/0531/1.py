n= int(input())
a, b= map(int, input().split())
m= int(input())
dp= [[1e9]*(n+1) for _ in range(n+1)]

for _ in range(m):
    v, v2= map(int, input().split())
    #edge[v].append(v2)
    #union(v,v2)
    dp[v][v2]=1
    dp[v2][v]=1

for v in range(1,n+1):
    dp[v][v]=0
for i in range(1,n+1):
    for j in range(1,n+1):
        for k in range(1,n+1):
            dp[j][k]= min(dp[j][k], dp[j][i]+dp[i][k])
if b<a:
    a,b= b,a
print([dp[a][b],-1][dp[a][b]==1e9])
#[print(*el[1:]) for el in dp[1:]]



'''
9
7 9
7
1 2
1 3
2 7
2 8
2 9
4 5
4 6
'''