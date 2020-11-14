from queue import PriorityQueue
import sys
'''
import queue as Q
q = Q.PriorityQueue()
'''
input = sys.stdin.readline

V, E = [int(i) for i in input().split()]
v = []
[v.append([]) for _ in range(V+1)]
K=int(input())

for _ in range(E):
    a, b, c = [int(i) for i in input().split()]
    v[a].append((c,b))

#print(v)
Q = PriorityQueue()
Q.put((0,K)) # w, edge
distance=[2e9]*(V+1)
distance[K]=0

while Q.empty()!=True:
    a = Q.get()

    if a[0]>distance[a[1]]: # (최저 가중치, 정점) 튜플이 아닌 스택은 버린다 
        a = Q.get()
    for (w, to) in v[a[1]]: 
 
        if distance[to] > a[0]+w:
            Q.put((a[0]+w, to))
            distance[to] = a[0]+w


[print('INF' if i==2e9 else i) for i in distance[1:] ] 

# priorityqueue 는 가중치 작은걸로 알아서 정렬해줌
'''
5 6
1
5 1 1
1 2 2
1 3 3
2 3 4
2 4 5
3 4 6

'''

