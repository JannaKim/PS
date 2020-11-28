from sys import *; input= lambda: stdin.readline().rstrip()

N = int(input())
T, P= [0], [0]
for _ in range(N):
    a, b = map(int, input().split())
    T.append(a)
    P.append(b)

dp=[0]*(N+1)
for i in range(1,N+1):
    if i-1+T[i]<=N:
        dp[i-1+T[i]]= max(P[i]+dp[i-1], dp[i-1+T[i]])
    dp[i]=max(dp[i-1],dp[i])

print(dp[N])
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