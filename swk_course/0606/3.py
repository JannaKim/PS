n = int(input())
edge = [ [] for _ in range(n + 1)]

P = [0] * (n + 1)
accum = [0] * (n + 1)
indegree = [0] * (n + 1)
start  = [True] * (n + 1)
for i in range(1 , n + 1):
    L = [*map(int ,input().split())]
    P[i] = L[0]
    accum[i] = L[0]
    if not L[1]:
        continue
    __ , __ , *nodes = L
    for el in nodes:
        indegree[i] += 1
        start[i] = False
        edge[el].append(i)

ans = 0

def dfs(v , pile):
    global ans
    for v2 in edge[v]:
        accum[v2] = max( P[v2] + pile , accum[v2] )
        indegree[v2] -= 1
        if not indegree[v2]:
            ans = max(ans , accum[v2])
            dfs(v2 , accum[v2])
#print(edge)
#print(indegree)
for v in range(1 , n + 1):
    if start[v]:
        ans = max(ans , accum[v])
        dfs(v , accum[v])
#print(accum)
print(ans)


'''
7
5 0
1 1 1
3 1 2
6 1 1
1 2 2 4
8 2 2 4
34 1 2
'''