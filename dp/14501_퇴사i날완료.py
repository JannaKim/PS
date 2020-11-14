N = int(input())
T = [0]*(N+1)
P = [0]*(N+1)

for i in range(1,N+1):
    T[i], P[i] = [int(i) for i in input().split()]


# dp[i]: i날에 완료되는 시간표 중 최대 수익
dp=[0]*(N+1+5)

for i in range(1,N+1):
    dp[i+T[i]-1] = max(dp[i+T[i]-1], dp[i-1]+P[i])
    dp[i] = max(dp[i-1], dp[i])

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

10
1 1
1 2
1 3
1 4
1 5
1 6
1 7
1 8
1 9
1 10
'''

'''
# dp[i]: i 날 전까지 끝나는 시간표들중 최대 이익 

dp=[0]*(N+1+10)

for i in range(1,N+1):
    dp[i+T[i]] = max(dp[i]+P[i], dp[i+T[i]]) 
    dp[i+1] = max(dp[i+1], dp[i])
print(dp[2:])
print(dp[N+1])
'''