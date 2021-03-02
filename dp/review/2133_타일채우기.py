# dp[i][0]: 하나만
# dp[i][1]: 두개만
# dp[i][2]: 다
n= int(input())
dp= [[0,0,0] for _ in range(max(3,n+1))]
dp[1][0]= 0
dp[1][1]= 2
dp[1][2]= 0

dp[2][0]= 2
dp[2][1]= 0
dp[2][2]= 3

for i in range(3,n+1):
    dp[i][0]= dp[i-1][1]
    dp[i][1]= dp[i-1][0]+ 2*dp[i-1][2]
    dp[i][2]= dp[i-2][2]+dp[i][0]
print(dp[n][2])

'''
3
0

4
11

5
0

6
41

7
0

8
153

12
2131
'''