from heapq import heappop , heappush
n , st , ed , m = map(int, input().split())
edge = [ set() for _ in range(n)]
for _ in range(m):
    a , b , c = map(int, input().split())
    edge[a].add( (b , c) )
P = [*map(int, input().split())]
stc = [n - 1] * n
dp = [-1e10] * n
q = []
heappush(q , (-P[st] , st))
dp[st] = P[st]
cycle = [False] * n
while q:
    p , v = heappop(q)
    p = -p
    #print(v , p)
    if dp[v] > p:
        continue

    if cycle[v]:
        for v2 , pri in edge[v]:
            if not cycle[v2]:
                cycle[v2] = True
                heappush(q , (-1e10 , v2))
        continue

    for v2 , pri in edge[v]:
        if P[v2] - pri + p > dp[v2]:
            stc[v2] -=1
            if stc[v2] < 0:
                continue
            if not stc[v2]:
                cycle[v2] = True
                
            dp[v2] = P[v2] - pri + p
            #print(dp)
            heappush(q , (-dp[v2] , v2) )

for _ in range(max(m , n)):
    for v in range(n):
        if cycle[v]:
            for v2 , pri in edge[v]:
                cycle[v2] = True
#print(cycle)
if cycle[ed]:
    print('Gee')

else:
    if dp[ed]== -1e10:
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