from heapq import heappush as push, heappop as pop
from fractions import *
T = int(input())
for _ in range(T):
    N, K = map(int,input().split())
    T = [0]+[int(i) for i in input().split()]
    edge =[[] for _ in range(N+1)]
    indegree=[-1]+[0]*N
    for _ in range(K):
        A, B = map(int, input().split())
        edge[B].append(A)
    W = int(input())

    
    accum=[-1]*(N+1)
    def heapq():
        global indegree
        q=[]
        push(q,(1e5-T[W], W))
        accum[W]=T[W]
        while q:
            reversed_time, building = pop(q)
            time = 1e5-reversed_time
            for v in edge[building]:
                indegree[v]-=1
                if indegree[v]==0:
                    
