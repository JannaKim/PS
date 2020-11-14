N = int(input())
P = [0]+[int(i) for i in input().split()]

dp = [0]+[10000]*(N)
for i in range(1,len(P)):
    for j in range(i,N+1):
        dp[j] = min(dp[j-i]+P[i], dp[j])

print(dp[N])

'''
4
1 5 6 7

5
10 9 8 7 6

10
1 1 2 3 5 8 13 21 34 55

10
5 10 11 12 13 30 35 40 45 47

4
3 5 15 16
'''
