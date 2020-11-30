import math
N = int(input())
P = [0]
for i in range(N):
    a, b = map(int, input().split())
    P.append(a)
    if i==N-1:
        P.append(b)

dp = [[0]*(N+1) for _ in range(N+1)]


for i in range(1,N):
    for j in range(1,N):
        if i+j>N:
            break
        dp[j][j+i]=math.inf
        for k in range(j,j+i):
            dp[j][j+i]=min(dp[j][j+i], dp[j][k]+dp[k+1][j+i]+P[j]*P[k+1]*P[j+i+1])
print(dp[1][N])



'''
6
2 1
5 1
3 1
5 1
10 1 
2 4
'''






# dp[a][b]: a

'''
import math

DP = [[0]*(n+1) for _ in range(n+1)]

for j in range(2,n+1): #대각선방향으로 눌러보자
    for i in range (j,n+1): 
        #print(j,"부터",n,"까지 도는중. 현재",i)
        #print("DP[",i-j+1,"][",i,"]=")
        print(f'DP[{i-j+1}][{i}]')
        DP[i-j+1][i] = math.inf # math module에서 제공하는 매우 큰 정수
        for k in range(i-j+1, i): 
            print(i-j+1,k,' ',k+1,i)
            cost = DP[i-j+1][k]+DP[k+1][i]+P[i-j+1]*P[k+1]*P[i+1]
            if DP[i-j+1][i]>cost:
                DP[i-j+1][i] = cost
        #print(DP[i-j+1][i])
print(DP[1][n])
'''
'''
for j in range(2,N+1): # 차이: 1~n-1까지 
    for i in range(j,N+1):
        dp[i-(j-1)][i] =1000*1000*1000
        for k in range(i-(j-1),i):
            print(i-(j-1), k, i)
            dp[i-(j-1)][i] = min(dp[i-(j-1)][i],     dp[i-(j-1)][k]    +dp[k+1][i]+         rc[i-(j-1)]*   rc[k]   *   rc[i])
'''




'''
3
5 3
3 2
2 6
'''


