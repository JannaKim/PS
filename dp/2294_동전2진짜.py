n, k = [int(i) for i in input().split()]
L=[]
for _ in range(n):
    L.append(int(input()))

dp=[0]+[k*2]*k
for won in L:
    for i in range(won,k+1):
        dp[i] = min(dp[i-won]+1, dp[i])

print(dp[k]) if dp[k]<2*k else print(-1)