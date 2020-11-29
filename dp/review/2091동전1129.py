X, *data = map(int, input().split())
unit = [1,5,10,25]

dp = [[0]*5 for _ in range(X+1)]

# dp[x][0~3] = x원 만드는 데 쓴 동전별 개수
# dp[x][4]: x원 만드는 데 쓴 최대 동전 개수
for i in range(4):
    for won in reversed(range(X+1)):
        if dp[won][4] or won==0: # won이 채워져 있거나 0원일 때
            for k in range(1,data[i]+1):
                if won+ unit[i]*k<=X and dp[won][4]+k>dp[won+ unit[i]*k][4]:
                    dp[won+ unit[i]*k][4]=dp[won][4]+k
                    for y in range(4):
                        dp[won+ unit[i]*k][y]=dp[won][y]
                    dp[won+ unit[i]*k][i]+=k

print(*dp[X][:4])


