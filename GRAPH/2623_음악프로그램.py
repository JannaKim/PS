N, M = map(int, input().split())
edge = [False] + [[] for _ in range(N)]
indegree = [-1]+[0]*N
for _ in range(M):
    L = [int(i) for i in input().split()]
    for i in range(1,len(L)-1):
        edge[L[i]].append(L[i+1])
        indegree[L[i+1]]+=1

stack = []
def indegree_BFS():
    q = [i for i in range(1,N+1) if indegree[i]==0]
    while q:
        v = q.pop(0)
        stack.append(v)
        for v2 in edge[v]:
            indegree[v2]-=1
            if indegree[v2]==0:
                q.append(v2)

indegree_BFS()
if len(stack)==N:
    [print(i) for i in stack]
else:
    print(0)

'''
6 3
3 1 4 3
4 6 2 5 4
2 2 3
'''

