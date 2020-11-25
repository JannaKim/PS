N, K = map(int, input().split())
WV = [(0,0)]
for _ in range(N):
    a, b = map(int,input().split())
    WV.append((a,b))

dp = []
for _ in range(N+1):
    dp.append([0]*(K+1))

for i in range(N+1):
    for j in range(1,K+1):
        
        if WV[i][0]<=j:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-WV[i][0]]+WV[i][1])
        else:
            dp[i][j] = dp[i-1][j]
print(dp[N][K])

'''
4 7
6 13
4 8
3 6
5 12
'''

