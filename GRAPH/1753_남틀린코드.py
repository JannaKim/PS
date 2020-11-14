import heapq
import sys

def Dijkstra(start):
    q = []
    d[start] = 0
    heapq.heappush(q,[0,start])
    while q:
        w,cnt=heapq.heappop(q)
        for node,w1 in graph[cnt]:
            temp=w1+w
            if temp < d[node]:
                d[node]=temp
                heapq.heappush(q,[w1,node])
    return

V,E=map(int,sys.stdin.readline().split())
start=int(sys.stdin.readline())
graph=[[] for _ in range(V+1)]
INF=sys.maxsize
for _ in range(E):
    u,v,w=map(int,sys.stdin.readline().split())
    graph[u].append([v,w])
d=[INF]*(V+1)

Dijkstra(start)
for i in range(1,len(d)):
    if d[i] == INF:
        print("INF")
    else:
        print(d[i])