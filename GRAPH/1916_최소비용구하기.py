#Dijikstra Algorithm
from heapq import heappush as push, heappop as pop
N = int(input())
edge = [False]+[[] for _ in range(N)]
M = int(input())
for _ in range(M):
    a, b, e = map(int, input().split())
    edge[b].append((e, a))

dep, arrv = map(int, input().split())

accum = [-1] + [int(1e5+1)*N]*N
def dijikstra(arrv):
    q = []
    push(q,(0,arrv))
    accum[arrv]=0
    while q:
        tmp, v = pop(q)
        if accum[v]<tmp:
            continue
        for dur, v2 in edge[v]:
            if dur+tmp<accum[v2]:
                accum[v2]=dur+tmp
                push(q,(accum[v2],v2))

dijikstra(arrv)
print(accum[dep])

'''
5
8
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
1 5
'''

