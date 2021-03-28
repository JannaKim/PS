import sys; input= lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(100000)
n= int(input())
edge=[[] for _ in range(n+1)]
indegree= [0]*(n+1)

for i in range(1,n+1):
    L= [*map(int, input().split())][1:]
    Len= len(L)
    for j in range(0,Len-1,2):
        if not j%2:
                edge[i].append((L[j], L[j+1]))
                indegree[L[j]]+=1
                indegree[i]+=1
ans=0
chk= [False]*(n+1)
def dfs(v,dist):
    global ans
    if not edge[v]:
        ans= max(ans, dist)
        return

    mx= max([indegree[v2]if not chk[v2] else 0 for v2,d in edge[v] ])
    if not mx:
        ans= max(ans, dist)
        return
        
    for v2,d in edge[v]:
        if indegree[v2]==mx:
            chk[v2]=True
            dfs(v2,dist+d)
            chk[v2]=False


for i in range(1,n+1):
    chk= [False]*(n+1)
    chk[i]=True
    dfs(i,0)
print(ans)



