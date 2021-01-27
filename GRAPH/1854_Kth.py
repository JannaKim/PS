from heapq import heappush, heappop
import sys; input= lambda: sys.stdin.readline().rstrip(); r=range

n, m, k= map(int, input().split())
edge= [[] for _ in r(n+1)]
for _ in r(m): 
    a, b, c= map(int, input().split())
    edge[a].append((b, c))

dur = [[] for _ in r(n+1)]
for i in r(1,n+1):
    for _ in r(k):
        heappush(dur[i], -1e9)
heappop(dur[1])
heappush(dur[1], 0)

q=[]
heappush(q, (0, 1))

while q:
    d, v= heappop(q)
    
    for v2, d2 in edge[v]:
        Kthdur= -heappop(dur[v2])
        if Kthdur> d+d2:
            Kthdur= d+d2
            heappush(q, (Kthdur, v2))
        heappush(dur[v2], -Kthdur)

for i in r(1,n+1):
    Kth=-heappop(dur[i])
    print([Kth,-1][Kth==1e9])

    