import math
T = int(input())
for _ in range(T):
    K = int(input())
    L = [int(i) for i in input().split()]
    dp=[[0]*K for _ in range(K)]
    cost=[[0]*K for _ in range(K)]
   
    for i in range(K):
        dp[i][i]=L[i]

    #[print(i) for i in dp]

    for i in range(1,K):
        for j in range(K-i):
            dp[j][j+i]=math.inf
            for k in range(j,j+i):
                #print(j,k,k+1,j+i)
                if dp[j][k]+dp[k+1][j+i]<=dp[j][j+i]:
                    dp[j][j+i] = dp[j][k]+dp[k+1][j+i]
                    cost[j][j+i] = min(cost[j][k]+cost[k+1][j+i] + dp[j][j+i],cost[j][j+i] if cost[j][j+i] else math.inf)
                    #print(f'cost[{j}][{j+i}] = cost[{j}][{k}]+cost[{k+1}][{j+i}] + {dp[j][j+i]}');
    #[print(i) for i in dp]
    #[print(i) for i in cost]

    print(cost[0][K-1])