
n , st , ed , m = map(int, input().split())

dp = [ [-1e9]* n for _ in range(n)]
cost = [ [1e9]* n for _ in range(n)]
for _ in range(m):
    a , b , c = map(int, input().split())
    cost[a][b] = min(cost[a][b] , c)
P = [*map(int, input().split())]

for i in range(n):
    dp[i][i] = P[i]
    for j in range(n):
        if cost[i][j] != 1e9:
            dp[i][j] = max(dp[i][j] , P[i]+P[j] - cost[i][j])
        
cycle = [ [False] * n for _ in range(n)]
for t in range(2):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if dp[j][i] != -1e9 and dp[i][k] != -1e9:
                    tmp = dp[j][i] + dp[i][k] - P[i]
                    if dp[j][k] < tmp:
                        if t == 1:
                            cycle[j][k] = True

                        dp[j][k] = tmp
#[print(*el) for el in dp]
for j in range(n):
    for k in range(n):
        if cycle[j][k]:
            if dp[st][j] != -1e9 and dp[k][ed] != -1e9:
                #print(j , k)
                cycle[st][ed] = True
if cycle[st][ed]:
    print('Gee')
else:
    print([dp[st][ed] , 'gg'][dp[st][ed]==-1e9])


'''
3 0 2 4
0 1 9999
1 2 9999
1 1 9999
0 2 0
10000 10000 10000


4 1 3 4 
0 1 0 
0 1 100000 
1 2 3 
2 3 4 
2 2 2 2

4 0 3 4 
0 1 0 
0 3 5 
1 2 0 
2 1 0 
0 5 5 10


5 0 4 6
0 1 10000
1 2 0
2 1 0
1 3 0
0 3 0
3 4 0
0 0 1 0 0

5 0 2 5
0 1 2
1 2 2
3 1 1
3 4 1
4 3 1
0 0 0 1 8

-4

4 1 3 4 
0 1 0 
0 1 100000 
1 2 3 
2 3 4 
2 2 2 2

-1

5 0 0 0
1 2 3 4 5
'''