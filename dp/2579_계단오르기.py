n_stairs=int(input())
#dp[i][0]= 지금계단은 안밟았을 때 최대 점수
#dp[i][1]= 1번 연속 올라갔을 때 최대 점수
#dp[i][2]= 2번 연속 올라갔을 때 최대 점수
dp=[[0,0,0]]
for i in range(1,n_stairs+1):
    point=int(input()) # 세 칸 이상 뛰는 거 안되는 거 주의
    dp.append([max(dp[i-1][1],dp[i-1][2]),dp[i-1][0]+point,dp[i-1][1]+point])

print(max(dp[n_stairs][1],dp[n_stairs][2]))
