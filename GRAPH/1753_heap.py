from heapq import heappush, heappop
import sys
'''
import queue as Q
q = Q.PriorityQueue()
'''
input = sys.stdin.readline

V, E = [int(i) for i in input().split()]
v = []
[v.append([]) for _ in range(V+1)]
K = int(input())

for _ in range(E):
    a, b, c = [int(i) for i in input().split()]
    v[a].append((c, b))

# print(v)

q = []
heappush(q, [0, K])  # w, edge

distance = [2e9]*(V+1)
distance[K] = 0

while q:
    cost, pos = heappop(q)

    if cost > distance[pos]:  # (최저 가중치, 정점) 튜플이 아닌 스택은 버린다
        continue
    for (w, to) in v[pos]:
        if distance[to] > cost+w:
            heappush(q, [cost+w, to])
            distance[to] = cost+w


[print('INF' if i == 2e9 else i) for i in distance[1:]]