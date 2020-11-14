N = int(input())
P = [0] + [int(i) for i in input().split()]

dp=[0]*(N+1)
for pack in range(1,N+1):
    for i in range(pack,N+1): 
        # 현재 pack을 한번이상 사고, 현재 팩과 그 이전의 팩들만을 사용해 구매하는 경우
        dp[i] = max(dp[i], P[pack]+dp[i-pack])

print(dp[N])

