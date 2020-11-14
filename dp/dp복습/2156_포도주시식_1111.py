N = int(input())
wine=[0]+[int(input()) for _ in range(N)]

#dp[N][2]
#dp[n][0]: n번째 포도주까지, 마지막꺼 안마셨을 때 마신 최대
#dp[n][1]: 마지막에 1잔
#dp[n][2]: 마지막에 2잔

dp=[[0]*3 for _ in range(N+1)]
for n in range(1,N+1):
    dp[n][0]=max(dp[n-1][0] if n>=2 else 0, dp[n-1][1] if n>=2 else 0, dp[n-1][2] if n>=3 else 0)
    dp[n][1]=(dp[n-1][0] if n>=2 else 0) +wine[n]
    dp[n][2]=(dp[n-1][1]if n>=2 else 0) +wine[n] if n>=2 else 0
print(dp)
print(max(dp[N]))
'''
6
6
10
13
9
8
1
'''