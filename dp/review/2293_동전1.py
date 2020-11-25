n, k = map(int, input().split())
won=[]
for _ in range(n):
    won.append(int(input()))

# dp[i][j]: i번째 동전까지만 사용해서 j원을 만드는 경우의 수
dp=[]
for i in range(n):
    dp.append([1] + [0]*k)
for i in range(n):
    for j in range(1, k+1):
        if j>=won[i]:
            dp[i][j] = dp[i][j-won[i]] + dp[i-1][j]
        else:
            dp[i][j] = dp[i-1][j]
print(dp[n-1][k])

'''
3 10
1
2
5
'''