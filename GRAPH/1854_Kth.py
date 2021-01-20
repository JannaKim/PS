from heapq import heappush, heappop

# ['', '', 'heappush(q, el)', 'heappop(q)']

n, m, k= map(int, input().split())

edge= [[] for _ in range(n+1)]

for _ in range(m): 
    a, b, c= map(int, input().split())
    edge[a].append((b, c))



accum= [[] for _ in range(n+1)]
q=[]
for v2, cost in edge[1]:
    heappush(q, (cost, v2))

while q:
    v, c= heappop(q)
    if len(accum[v])<k:
        accum[v].append()