import math
N, M = map(int, input().split())
L=[int(i) for i in input().split()]
C=[int(i) for i in input().split()]

dp=[[[0,0] for _ in range(2)] for __ in range(N)]

dp[0][0]= [L[0], C[0]]
dp[0][1]= [0,math.inf]

mn= math.inf
for i in range(1,N):
    prv= dp[i-1]
    if prv[1][0]+ L[i]>=M: 
        mn = min(mn, prv[1][1]+C[i])
        dp[i][0]=dp[i-1][0]
    else: 
        if prv[1][1]+ C[i]<prv[0][1]+ C[i]:
            dp[i][0]= [prv[1][0]+ L[i],prv[1][1]+ C[i]]
        else:
            dp[i][0]= [prv[0][0]+ L[i],prv[0][1]+ C[i]]
    if prv[0][0]+ L[i]>=M: mn = min(mn, prv[0][1]+C[i])
    else: dp[i][0]= [prv[0][0]+ L[i],prv[0][1]+ C[i]]

    if prv[0][1]<prv[1][1]:
        dp[i][1]= [prv[0][0],prv[0][1]]
    else:
        dp[i][1]= [prv[1][0],prv[1][1]]

    print(dp[i])

print(mn)
