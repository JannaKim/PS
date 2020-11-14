
N, K = [int(i) for i in input().split()]
WT=[0]*N
val=[0]*N
for i in range(N):
    WT[i], val[i] = [int(i) for i in input().split()]


# dp[i][j]: 1~i까지의 물건을 무게 j 이하로 가져갔을 때 
#                                        챙겨갈 최대 가치
print(WT)
print(val)
dp=[]
for _ in range(N):
    dp.append([0]*(K+1))
for i in range(N):
    for j in range(1, K+1):
        if WT[i]<=j:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-WT[i]]+val[i])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[N-1][K])
print(dp)

'''
4 3
2 7
1 9
1 9
1 9
'''
