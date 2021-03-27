x, a, b, c, d =map(int, input().split())

unit= [1,5,10,25]
maxi= [a,b,c,d]

dp= [[0,0,0,0,0] for _ in range(x+1)]

for idx, won in enumerate(unit):
    for i in range(x,-1,-1):
        for num in range(1,maxi[idx]+1):
            if not i or dp[i][4]:
                if i+won*num<=x:
                    if dp[i+won*num][4]<dp[i][4]+num:
                        dp[i+won*num][4]=dp[i][4]+num
                        for j in range(4):
                            dp[i+won*num][j]=dp[i][j]
                        dp[i+won*num][idx]+=num
print(*dp[x][:-1])
