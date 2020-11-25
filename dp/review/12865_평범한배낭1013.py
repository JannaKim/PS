N, K = [int(i) for i in input().split()]

wt=[0]*N
vl=[0]*N

for i in range(N):
    wt[i], vl[i] = [int(j) for j in input().split()]

# dp[i][j]: 0~i 물건들 중에서 무게 j 이하로 가져갈 때 가져갈 수 있는 최대 가치

dp=[]
for _ in range(N):
    dp.append([0]*(1+K))

for i in range(N):
    for j in range(1,K+1):
        #print(f'dp[{i}][{j}]')
        if wt[i]<=j:
            #print(f'dp[{i}][{j}] = max(dp[{i-1}][{j}], dp[{i-1}][{j-wt[i]}] + vl[{i}]) ')
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-wt[i]] + vl[i])
        elif wt[i]>j: # ★★★★★★★★★★★★★★★★★
            dp[i][j] = dp[i-1][j]

print(dp[N-1][K])

'''
4 7
6 13
4 8
3 6
5 12
'''
