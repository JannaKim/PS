from heapq import heappop , heappush
n , st , ed , m = map(int, input().split())
edge = [ [] for _ in range(n)]
for _ in range(m):
    a , b , c = map(int, input().split())
    edge[a].append( (b , c) )
P = [*map(int, input().split())]
stc = [2*n] * n
dp = [-1e10] * n
q = []
heappush(q , (-P[st] , st))
dp[st] = P[st]
cycle = [False] * n
while q:
    p , v = heappop(q)
    p = -p
    if dp[v] > p:
        continue

    for v2 , pri in edge[v]:
        if P[v2] - pri + p > dp[v2]:
            dp[v2] = P[v2] - pri + p
            stc[v2] -=1
            if not stc[v2]:
                cycle[v2] = True
            if stc[v2] < 0:
                continue
            #print(dp)
            heappush(q , (-dp[v2] , v2) )

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

#print(cycle)
for v in range(n):
    chk = [False]*n
    if cycle[v]:
        chk[v] = True
        dfs(v)
if cycle[ed]:
    print('Gee')
elif dp[ed]== -1e10:
    print('gg')                 

else:
    print(dp[ed])



'''
3 0 2 4
0 1 9999
1 2 9999
1 1 9999
0 2 0
10000 10000 10000


4 0 3 4 
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

5

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

3 0 2 3
0 1 5
0 2 2
1 2 -10
0 0 0
'''