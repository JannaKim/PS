n , m = map(int, input().split())
mp = [ [*map(int, input().split())] for _ in range(n)]

dp = [ [0]* m for _ in range(n)]
for i in range(n):
    s = 0
    for j in range(m):
        if i:
            dp[i][j] += dp[i-1][j]
        dp[i][j] += mp[i][j] + s
        s += mp[i][j]

#print(*dp , sep = '\n')
k = int(input())
for _ in range(k):
    a , b , c , d = [int(i)-1 for i in input().split()]
    ans = dp[c][d]
    if a:
        ans -= dp[a-1][d]
    if b:
        ans -= dp[c][b-1]
    if a and b:
        ans += dp[a-1][b-1]
    print(ans)
