'''
dp[i][0]: not big jumped
dp[i][1]: big jumped
'''

n = int(input())
dp = [[1e9] * 2 for _ in range(n + 1)]

dp[1] = [0, 1e9]
jump = []
jump.append( (0,1e9))
for _ in range(n-1):
    a, b = map(int, input().split())
    jump.append(( a, b) )

k = int(input())
for i in range(1 , n):
    if i + 1 <= n:
        dp[i + 1][0] = min(dp[i + 1][0], dp[i][0] + jump[i][0])
        dp[i + 1][1] = min(dp[i + 1][1], dp[i][1] + jump[i][0])
    if i + 2 <= n:
        dp[i + 2][0] = min(dp[i + 2][0], dp[i][0] + jump[i][1])
        dp[i + 2][1] = min(dp[i + 2][1], dp[i][1] + jump[i][1])
    if i + 3 <= n:
        dp[i + 3][1] = min(dp[i + 3][1], dp[i][0] + k)

    #for el in dp[1:]:
    #    print(*el)
    #print()

print(min(dp[n]))