N = int(input())
P = [int(i) for i in input().split()]

# dp[i]:i개를 1~i개 조합으로 만들 수 있는 경우들
# dp[i]를 1~pack 사이 팩을 써서 만들수 있는 금액의 최대값
'''
4
1 5 6 7
'''
dp=[0]*(N+1)

for pack in range(1,N+1):
    for i in range(pack,N+1): # pack 을 반드시 한번 쓰고 그 이하의 pack들로 i만들기
        a = P[pack-1]+dp[i-pack]
        dp[i]= max(dp[i], a)

print(dp[N])
