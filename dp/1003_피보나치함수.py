# dp[i][j]: fib(i) 가 호출하는 fib(j)의 수
# dp[i][j]=(dp[i-1][0]+dp[i-2][0], dp[i-1][1]+dp[i-2][1])
# 이전, 이전이전 호출해서 더하면 된다.

    
T = int(input())
for _ in range(T):
    dp=[(1,0), (0,1)]
    N=int(input())
    if N<=1:
        print(dp[N][0], dp[N][1])
    else:
        for i in range(2,N+1):
            dp.append((dp[i-1][0]+dp[i-2][0], dp[i-1][1]+dp[i-2][1]))
        print(dp[N][0], dp[N][1])
