import sys; input= lambda: sys.stdin.readline().rstrip()
from heapq import heappush, heappop
n, m= map(int, input().split())

edge= [[] for _ in range(n+1)]
for _ in range(m):
    a, b= map(int ,input().split())
    edge[a].append(b)
    edge[b].append(a)

accum= [1e9]*(n+1)
def bfs(st):
    q=[]
    heappush(q, [0,st])
    while q:
        dist, v= heappop(q)
        #print(dist,v)
        #print(v,dist)
        if accum[v]<dist:
            continue
            #print(f'accum[{st}]=accum[{v}]+{dist}')

        for v2 in edge[v]:
            if dist+1<accum[v2]:
                accum[v2]=dist+1
                heappush(q, [accum[v2],v2])
        
ans=1e9
loc=[0,0]
for i in range(1,n+1):
    for j in range(i+1,n+1):
        accum= [1e9]*(n+1)
        accum[i]=0
        accum[j]=0
        bfs(i)
        bfs(j)
        s=sum(accum[1:])*2
        if s<ans:
            ans=s
            loc=[i,j]

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