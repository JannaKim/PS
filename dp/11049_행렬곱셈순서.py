N = int(input())
rc = [1]
for i in range(N):
    a, b = map(int, input().split())
    rc.append(a)
    if i==N-1:
        rc.append(b)

print(rc)
'''
앞 rc[0] * 앞 rc[1] * 뒤 rc[1]

dp [rc[0][0]] [rc[N-1][1]] 이 답

dp[i][j]계산했을 때 최소 연산횟수

'''

dp = [[0]*(N+1) for _ in range(N+1)]
# dp[a][b]: a
for j in range(2,N+1): # 차이: 1~n-1까지 
    for i in range(j,N+1):
        dp[i-(j-1)][i] =1000*1000*1000
        for k in range(i-(j-1),i):
            print(i-(j-1), k, i)
            dp[i-(j-1)][i] = min(dp[i-(j-1)][i],     dp[i-(j-1)][k]    +dp[k+1][i]+         rc[i-(j-1)]*   rc[k]   *   rc[i])

print(dp)
print(dp[1][N])


'''
3
5 3
3 2
2 6
'''


