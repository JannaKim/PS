import sys; input= lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(100000)
from heapq import heappush, heappop
n, m= map(int, input().split())

edge= [[] for _ in range(n+1)]
for _ in range(m):
    a, b= map(int ,input().split())
    edge[a].append(b)
    edge[b].append(a)

chk= [False]*(n+1)
ans=1e9
loc=[0,0]
traveled=[False]*(n+1)
accum= [-1]*(n+1)
def bfs(st):
    q=[]
    heappush(q, [0,st])
    while q:
        dist, v= heappop(q)
        #print(v,dist)
        if chk[v]:
            accum[v]= dist
            return dist
        if accum[v]>=0:
            #print(f'accum[{st}]=accum[{v}]+{dist}')
            accum[st]=accum[v]+dist
            return accum[st]
        if traveled[v]:
            continue
        traveled[v]=True
        for v2 in edge[v]:
            if not traveled[v2]:
                heappush(q, [dist+1,v2])
        

for i in range(1,n+1):
    chk[i]=True
    for j in range(i+1,n+1):
        chk[j]=True
        s=0
        accum= [-1]*(n+1)
        accum[i]=0
        accum[j]=0
        for k in range(1,n+1):
            traveled=[False]*(n+1)
            s+=(bfs(k)*2)
        if s<ans:
            ans=s
            loc=[i,j]
        chk[j]=False
    chk[i]=False

print(*loc, ans)


'''
9 9
1 2
2 3
3 4
4 5
5 7
7 9
5 6
6 7
6 8
'''