'''
dp[i][0]: 위아래
dp[i][1]: 가운데 두개
dp[i][2]: 위나 아래 두개
dp[i][3]: 다채움
'''

dp= [[0,0,0,0] for _ in range(23)]
dp[1][0]= 0
dp[1][1]= 1
dp[1][2]= 2
dp[1][3]= 1

dp[2][0]= 1
dp[2][1]= 1
dp[2][2]= 4
dp[2][3]= 5

for i in range(3, 23):
    dp[i][0]=dp[i-1][1]
    dp[i][1]=dp[i-1][3]+ dp[i-1][0]
    dp[i][2]=2*dp[i-1][3]+dp[i-1][2]
    dp[i][3]=dp[i-1][1]+ dp[i-1][2]+dp[i-1][3]+dp[i-2][3]

for _ in range(int(input())):
    n= int(input())
    print(dp[n][3])
