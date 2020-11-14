# dp[i]: 3*i 블록에 아래와 같이 블록을 넣을 수 있는 경우의 수
# dp[i][0]: i-1까진 다 채우고 i번째 블록이 다 차있을때
# dp[i][1]: i-1까진 다 채우고 i번째 블록이 위에 두개만
# dp[i][2]: i-1까진 다 채우고 i번째 블록이 아래 두개만

N = int(input()) # 1<= N <= 30
dp=[[0,1,1],[3,0,0]]
if N==1:
    print(0)
else:
    for i in range(2,N):
        dp.append([0]*3)
        #if i!=N-1:
        dp[i][0]= dp[i-2][0]+ dp[i-1][1]+ dp[i-1][2]
        dp[i][1]= dp[i-2][1]+ dp[i-1][0]
        dp[i][2] =dp[i-2][2]+ dp[i-1][0]
        #else:
        #    dp[i]=dp[i-1][1]+dp[i-1][2]
        #print(dp)
    print(dp[N-1][0])

# C:\Users\OEJ\Desktop\동민쌤수업\dp\dp풀이사진
# https://www.acmicpc.net/problem/2133
 