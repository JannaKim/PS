n , st , ed , m = map(int, input().split())
dp = [-1e9] * n # st - >  i 최대 버는 돈
edge = [ [] for _ in range(n) ]
for _ in range(m):
    a, b , c = map(int, input().split())
    edge[a].append((b , c))

P = [*map(int, input().split())]
dp[st] = P[st]

chk = [False]*n
def dfs(v):
    found = False
    for v2 ,c in edge[v]:
        if not chk[v2]:
            chk[v2] = True
            if v2 == ed:
                return  True
            found |= dfs(v2)
    return found

def BF():
    for t in range(1 , n + 1):
        for v in range(n):
            for v2 , cst in edge[v]:
                if dp[v] != -1e9 and dp[v] - cst + P[v2] > dp[v2]:
                    if t == n:
                        chk = [False]*n
                        chk[v2] = True
                        if dfs(v2):
                            
                            return 'Gee'
                    dp[v2] = dp[v] - cst + P[v2]

    return [ dp[ed] , 'gg'][dp[ed] == -1e9]

print(BF())
# 154 47 69 12260529
'''
3 0 2 4
0 1 9999
1 2 9999
1 1 9999
0 2 0
10000 10000 10000
 4 %

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
'''