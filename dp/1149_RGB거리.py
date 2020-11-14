N = int(input())
#dp[i][0]: i번째 집까지,끝에 빨강을 칠했을 때 최소 비용
#dp[i][1]: i번째 집까지,끝에 초록을 칠했을 때 최소 비용
#dp[i][2]: i번째 집까지,끝에 파랑을 칠했을 때 최소 비용

dp=[[int(i) for i in input().split()]]

for i in range(1,N):
    R,G,B=[int(j) for j in input().split()]
    dp.append([min(dp[i-1][1],dp[i-1][2])+R, min(dp[i-1][0],dp[i-1][2])+G, min(dp[i-1][0],dp[i-1][1])+B])

#print(dp)
print(min(dp[N-1]))

'''
3
26 40 83
49 60 57
13 89 99
'''