r= range
n, m= map(int, input().split())

table= [[0]*(n+2)]
table+= [[0]+[int(i) for i in input().split()]+[0] for _ in r(n)]
table+= [[0]*(n+2)]

[print(*el) for el in table]
dp= [[0]*(n+2) for _ in r(n+2)]
prv=0
for i in r(n*n):
    
    row= i//n+1
    col= i%n+1
    print(row, col)
    dp[row][col]= prv+table[row][col]
    prv= dp[row][col]


for _ in r(m):
    a, b, c, d= map(int, input().split())
    print(dp[c][d]-dp[a][b]+table[a][b])