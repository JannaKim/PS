N = int(input())
T=[0]
P=[0]
for _ in range(N):
    a, b=map(int, input().split())
    T.append(a)
    P.append(b)

dp=[0]*(N+10)
#dp[i]: i날을 끝으로상담 마친것까지 해서 최대 이익
for i in range(1,N+1):

    dp[i-1+T[i]] = max(dp[i-1+T[i]] ,dp[i-1]+P[i])
    dp[i]=max(dp[i],dp[i-1])
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