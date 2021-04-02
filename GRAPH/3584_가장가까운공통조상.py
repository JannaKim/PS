import sys; input= lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10000)
for _ in range(int(input())):
    n= int(input())
    edge=[0]*(n+1)
    down=[[] for _ in range(n+1)]
    indegree= [0]*(n+1)
    deg= [0]*(n+1)
    for _ in range(n-1):
        a, b= map(int, input().split())
        edge[b]=a
        down[a].append(b)
        indegree[b]+=1

    def dfs(v, d):
        for v2 in down[v]:
            deg[v2]=d
            dfs(v2, d+1)

    for i in range(1,n+1):
        if not indegree[i]:
            dfs(i,1)
            break

    def up(v,cnt):
        if not cnt:
            return v
        return up(edge[v],cnt-1)

    
    a, b=map(int, input().split())
    A, B= a ,b
    print(deg)
    if deg[a]>deg[b]:
        B= up(b, deg[a]-deg[b])
    elif deg[a]<deg[b]:
        B= up(a, deg[b]-deg[a])
    while A!=B:
        A= up(A, 1)
        B= up(B, 1)
    print(A)

