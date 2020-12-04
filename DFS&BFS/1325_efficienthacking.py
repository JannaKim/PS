import sys; sys.setrecursionlimit(1000000)
input = lambda: sys.stdin.readline()
N, M = map(int, input().split())
edge = [[] for _ in range(N+1)]
indegree = [0]*(N+1)
for _ in range(M):
    a, b = map(int, input().split())
    edge[b].append(a)
    indegree[a]+=1

check = [False]*(N+1) # uninitialize visited array?
def dfs(v):
    global cnt
    for v2 in edge[v]:
        if not check[v2]:
            cnt+=1
            check[v2]=True
            dfs(v2)



cnt=1
ans=[]
mx=-1
for i in range(1,N+1):
    if not indegree[i]:
        dfs(i)
        mx = max(mx, cnt)
        ans.append((i, cnt))
        check = [False]*(N+1)
        cnt=1
A = []
[A.append(str(el[0])) for el in ans if el[1]==mx]
print(" ".join(A))
        


'''
5 4
3 1
3 2
4 3
5 3
'''