import sys; input=lambda: sys.stdin.readline().rstrip()
N, M = map(int,input().split())
edge=[[] for _ in range(N+1)]
indegree=[0]*(N+1)
for _ in range(M):
    a, b = map(int, input().split())
    edge[a].append(b)
    indegree[b]+=1
stack=[]
Q=[]
def line():
    for i in range(1,N+1):
        if indegree[i]==0:
            Q.append(i)
    while Q:
        n=Q.pop(0)
        stack.append(n)
        for v2 in edge[n]:
            indegree[v2]-=1
            if indegree[v2]==0:
                Q.append(v2)
line()
print(*stack)

'''
3 2
1 3
2 3
'''