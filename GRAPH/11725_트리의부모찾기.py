import sys; input= lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(100000)
n= int(input())
edge= [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b= map(int, input().split())
    edge[a].append(b)
    edge[b].append(a)

chk=[False]*(n+1)
root= [0]*(n+1)
def dfs(v):
    for v2 in edge[v]:
        if not chk[v2]:
            chk[v2]=True
            root[v2]=v
            dfs(v2)



chk[1]=True
dfs(1)

for v in range(2,n+1):
    print(root[v])