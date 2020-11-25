import sys
f = sys.stdin
N = int(f.readline()) 
TP=[(0,0)]
for _ in range(N):
    TP.append(tuple(map(int,f.readline().split())))
    

#dp[i]: i일 끝까지 상담 셰쥴 짰을 때 받을 수 있는 최대 금액
dp = [0]*(N+1+5)
for i in range(1, N+1):
    dp[i+TP[i][0]-1] = max(dp[i-1]+TP[i][1], dp[i+TP[i][0]-1])
    dp[i] = max(dp[i], dp[i-1])

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