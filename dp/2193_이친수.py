N=int(input())
if N<=2:
    print(1)
else:
    # dp[i][0]: 0으로 끝나는 i자리 이친수 개수
    # dp[i][1]: 1로 끝나는 i자리 이친수 개수
    dp=[(0,0),(0,1), (1,0)] # 이친수는 무조건 10으로 시작해야 하므로 dp[2]까진 고정
    for i in range(3,N+1):
        dp.append((dp[i-1][0]+dp[i-1][1], dp[i-1][0]))


    print(dp[N][0]+dp[N][1])