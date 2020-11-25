N, K = map(int, input().split())
wv=[]
for _ in range(N):
    wv.append(tuple(int(i) for i in input().split()))

dp = [[0]*(K+1) for _ in range(N)]

for i in range(N):
    for j in range(1,K+1):
        if wv[i][0]<=j:
            dp[i][j] = max(dp[i-1][j-wv[i][0]]+wv[i][1], dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]
print(dp[-1][K])

'''
4 7
6 13
4 8
3 6
5 12
'''