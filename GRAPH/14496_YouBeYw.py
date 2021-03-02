from heapq import heappop, heappush
# a -> b 로 가는 최단 경로

a, b= [int(i)-1 for i in input().split()]
n, m= map(int, input().split())

edge= [[] for _ in range(n)]
for _ in range(m):
    x, y= [int(i)-1 for i in input().split()]
    edge[x].append(y)
    edge[y].append(x)

dur= [1e9]*n
dur[a]=0
q=[]
heappush(q, (0,a))
while q:
    cost, v= heappop(q)
    if dur[v]<cost:
        continue
    for v2 in edge[v]:
        if 1+cost<dur[v2]:
            dur[v2]=1+cost
            heappush(q, (dur[v2],v2))
print([dur[b],-1][dur[b]==1e9])

