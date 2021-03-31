import sys; input= lambda: sys.stdin.readline().rstrip()
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
    flag=False
    for v2,d in edge[v]:
        if not chk[v2]:
            flag=True
            chk[v2]=True
            dfs(v2,dist+d)
            chk[v2]=False
    if not flag:
        global ans
        ans= max(ans, dist)
#print(indegree)
for i in range(1,n+1):
    if indegree[i]==2:
        chk[i]=True
        dfs(i,0)
        chk[i]=False
print(ans)