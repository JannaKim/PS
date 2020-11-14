n = int(input())
wine=[]
for i in range(n):
    wine.append(int(input()))

dp=[]
for i in range(n):
    dp.append([0,0,0])

dp[0][0]=0
dp[0][1]=wine[0]
dp[0][2]=wine[0]


'''
B=[wine[0],0,wine[0]+wine[2]]# 시작이 oxo, 끝이 xo
C=[wine[0],0]# 시작이 ox, 끝이 xx
D=[wine[0],wine[0]+wine[1],0]# 시작이 oox, 끝이 xox
'''

if n==1:
    print(wine[0])
elif n==2:
    print(wine[0]+wine[1])
else:
    dp[1][0]=wine[0]
    dp[1][1]=wine[1]
    dp[1][2]=wine[0]+wine[1]
    
    for i in range(2,n):
        #print(i, ',',[dp[i-1][0],dp[i-1][1],dp[i-1][2]])
        dp[i][0]=max([dp[i-1][0],dp[i-1][1],dp[i-1][2]])
        dp[i][1]=dp[i-1][0]+wine[i]
        dp[i][2]=dp[i-1][1]+wine[i]

    print(max([dp[n-1][0],dp[n-1][1],dp[n-1][2]]))

    '''
    xoo
    oxo
    oox
    '''
