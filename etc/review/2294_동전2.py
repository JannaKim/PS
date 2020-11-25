n, k = map(int, input().split())
won = [int(input()) for i in [0]*(n)]

# dp[i]:i원을 만드는 데 드는 최소 동전 개수
dp=[0]+[2*k]*k
for w in won:
    for i in range(1,k+1):
        if k-w>=0:
            dp[i]=min(dp[i],dp[i-w]+1)

print(dp[k] if dp[k]!=2*k else -1)
