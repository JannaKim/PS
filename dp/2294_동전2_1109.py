n, k = map(int, input().split())
coin = []
[coin.append(int(input())) for _ in range(n)]

dp = [0]+[k+1]*(k)
for i in coin:
    for j in range(i,k+1):
        dp[j] = min(dp[j], dp[j-i]+1)
[print(dp[k]) if dp[k]<k+1 else print(-1)]

'''
3 15
1
5
12
'''