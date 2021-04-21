n= int(input())

dp=[[1e10]*5 for _ in range(n+1)]
loc=[]
dp[0]=[0]*5
for _ in range(n+1):
    x, y= map(int, input().split())
    loc.append((x,y))
dx= [0,1, -1, 0, 0]
dy= [0,0, 0, 1, -1]

for i in range(1,n+1):
    for k in range(5):
        for j in range(5):
            #print(loc[i-1][0]+(dx[j] if i!=1 else 0),loc[i-1][1]+(dy[j] if i!=1 else 0),'->',loc[i][0]+dx[k],loc[i][1]+dy[k], '=',dp[i-1][j]+abs((loc[i-1][0]+(dx[j] if i!=1 else 0))-(loc[i][0]+dx[k]))+abs((loc[i-1][1]+(dy[j] if i!=1 else 0))-(loc[i][1]+dy[k])))
            dp[i][k]= min(dp[i][k], dp[i-1][j]+abs((loc[i-1][0]+(dx[j] if i!=1 else 0))-(loc[i][0]+dx[k]))+abs((loc[i-1][1]+(dy[j] if i!=1 else 0))-(loc[i][1]+dy[k])))
    #print(dp[i])
    #print()

#[print(*el) for el in dp]
print(min(dp[n]))

#long long= 100경