n = int(input())
wine=[]
wine.append(int(input())) # 첫번째 잔

dp=[]
dp.append([0, wine[0], wine[0]])


if n==1:
    print(max(dp[n-1]))
else:
    for i in range(1,n):
        wine.append(int(input()))
        dp.append([max(dp[i-1]),dp[i-1][0]+wine[i],dp[i-1][1]+wine[i]])
        
    print(max(dp[n-1]))

