N=int(input())
# dp[i][0]: 끝이 0인 총 계단수
# dp[i][9]: 끝이 9인 총 계단수

dp=[[0,1,1,1,1,1,1,1,1,1]]
for i in range(1,N):
    dp.append([dp[i-1][1]])
    for j in range(1,9):
        dp[i].append(dp[i-1][j-1]+dp[i-1][j+1])
    dp[i].append(dp[i-1][8])

print(sum(dp[N-1])%1e9) # Q) 1e9: 실수. 정수로 감싸야한다

