n= int(input())

dp=[-1]*(n+1+4)
dp[1]=1
dp[3]=1
dp[4]=1
turn=True
for i in range(2,n+1):
    if turn:
        turn=False
        rock=0
    else:
        turn=True
        rock=1
    for j in range(n,0,-1):
        if dp[j]==rock^1:
            dp[j]=-1
            dp[j+1]=rock
            dp[j+3]=rock
            dp[j+4]=rock
    print(dp)
skWins=True

if dp[n]==0:
    print('CY')
else:
    print('SK')