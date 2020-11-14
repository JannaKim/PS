N = int(input())
cnslt=[]
for _ in range(N):
    cnslt.append([int(i) for i in input().split()])

dp=[0]*(N + 15)

for i in range(N):
    if dp[i + cnslt[i][0]] < dp[i] + cnslt[i][1]:
        dp[i + cnslt[i][0]] = dp[i] + cnslt[i][1]
    if dp[i] > dp[i + 1]:
        dp[i + 1] = dp[i]

print(max(dp[:N + 1]))

'''
7
3 10
5 20
1 10
1 20
2 15
4 40
2 200
'''