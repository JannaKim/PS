N, E = map(int,input().split())
edge = [[] for _ in range(N+1)]
indegree = [-1] + [0]*N
for _ in range(E):
    A, B = map(int, input().split())
    edge[A].append(B)
    indegree[B]+=1

print(edge)
visited= [True] + [False]*N
Q=[]
def dfs(v):
    global Q
    visited[v]=True
    for node in edge[v]:
        if not visited[node]:
            #print(f'{"  "}dfs({node})')
            dfs(node)
    Q = [v] + Q

for i in range(1,N+1):
    if indegree[i]==0:
        dfs(i)
print(Q)
    
        




'''
7 8
1 3
1 2
1 4
2 5
5 7
3 5
3 6
6 2


9 8
8 9
8 7
6 7
6 5
5 4
3 4
3 2
2 1
'''