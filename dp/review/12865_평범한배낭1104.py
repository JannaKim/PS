N, K = map(int, input().split())
P = []
for _ in range(N):
    a, b = map(int, input().split())
    P.append((a,b))

# dp[i][j]: 0~i 물건들 중에서 무게 j 이하로 가져갈 때 가져갈 수 있는 최대 가치
dp = []
[dp.append([0]*(K+1)) for _ in range(N)]
for i in range(N):
    for j in range(K+1):
        if P[i][0]<=j:
            dp[i][j] = max(dp[i-1][j-P[i][0]] + P[i][1], dp[i-1][j] )
        else:
            dp[i][j] = dp[i-1][j]

        print(f'dp[{i}][{j}]={dp[i][j]}')
print(dp)
print(dp[N-1][K])

'''
4 7
6 13
4 8
3 6
5 12
'''