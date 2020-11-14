N = int(input())
P=[0]+[int(i) for i in input().split()]

#dp[i]: 카드 i개를 구매할때 최대 금액

dp=[0]*(N+1)
for i in range(1,N+1):
    for j in range(i,N+1):
        dp[j] = max(dp[j] , dp[j-i]+P[i])

print(dp[N])

'''
4
1 5 6 7
'''