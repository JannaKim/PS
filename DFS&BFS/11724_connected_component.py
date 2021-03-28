n, m= map(int, input().split())

edge= [[] for _ in range(n+1)]

for _ in range(m):
    a, b= map(int, input().split())
    edge[a].append(b)
    edge[b].append(a)

chk= [True]+[False]*n



def dfs(v):
    chk[v]=True
    for v2 in edge[v]:
        if not chk[v2]:
            dfs(v2)

cnt=0         
for i in range(1,n+1):
    if not chk[i]:
        cnt+=1
        dfs(i)
print(cnt)