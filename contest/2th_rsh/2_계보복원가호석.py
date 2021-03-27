import sys; input= lambda: sys.stdin.readline().rstrip()
n= int(input())
indegree=[0]*n
edge= [[] for _ in range(n)]
change={}
rev={}
for idx,el in enumerate(sorted(input().split())):
    change[el]=idx
    rev[idx]=el
m= int(input())
for _ in range(m):
    a, b= input().split()
    indegree[change[a]]+=1
    edge[change[b]].append(change[a])

gamoon=0
ans=[]
written= [False]*n
def dfs(v):
    if written[v]:
        return
    written[v]=True
    edge[v].sort()
    jikgae=[]
    Len=0
    for v2 in edge[v]:
        if indegree[v2]-indegree[v]==1:
            Len+=1
            jikgae.append(v2)
    ans.append([v,Len]+jikgae)
    for v2 in edge[v]:
        dfs(v2)

gamoons=[]
for i in range(n):
    if not indegree[i]:
        gamoons.append(i)
        gamoon+=1
        dfs(i)

print(gamoon)
for el in gamoons:
    print(rev[el],end=' ')
print()
for el in sorted(ans):
    print(rev[el[0]], el[1],end=' ')
    for a in el[2:]:
        print(rev[a],end=' ')
    print()

