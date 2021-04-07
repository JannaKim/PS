import sys; input= lambda: sys.stdin.readline().rstrip()
from collections import deque
n= int(input())
edge=[[] for _ in range(n+1)]
deg= [0]*(n+1)

for v in range(1,n+1):
    L=[*map(int, input().split())]
    for i in range(1,n*2+1,2):
        if L[i]==-1:
            break
        edge[v].append((L[i], L[i+1]))
        deg[v]+=1
        deg[L[i]]+=1

ans=0
for i in range(1,n+1):
    if deg[i]==2:
        q=deque()
        q.append((i,0,0))
        #print(i,'->')
        while q:
            v, prv, d= q.popleft()
            for v2, d2 in edge[v]:
                if v2!=prv and deg[v2]!=2:
                    q.append((v2,v,d+d2))
                elif v2!=prv and deg[v2]==2:
                    ans= max(v,d+d2)
print(ans)

'''
cmd t
cmd 1
pwd
cmd space
'''