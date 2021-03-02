n= int(input())
dp= [[0]*4 for _ in range(max(n,3)+1)]
'''
dp[i][0]: i째가 위가 1*2짜리로 삐져나옴
dp[i][1]: i째가 아래가 1*2짜리로 삐져나옴
dp[i][2]: i째가 다 참, 끝에가 2*1 또는 1*1 두 개
dp[i][3]: i쨰가 1*2 두개로 채워져있음
'''


dp[1][0]= 0
dp[1][1]= 0
dp[1][2]= 2
dp[1][3]= 0
dp[2][0]= 1
dp[2][1]= 1
dp[2][2]= dp[1][2]*2+ dp[1][0]*2+ dp[1][1]*2
dp[2][3]=1

# dp[2]의 합? sum[dp[2]]+1 (예외 케이스.)

if n==1:
    print(sum(dp[1]))
    exit()
if n==2:
    print(sum(dp[2]))
    exit()
for i in range(3, n+1):
    dp[i][0]= dp[i-1][2]//2+ dp[i-1][1]
    dp[i][1]= dp[i-1][2]//2+ dp[i-1][0]
    dp[i][2]= sum(dp[i-1])*2
    dp[i][3]= sum(dp[i-2])
print(sum(dp[n]))

