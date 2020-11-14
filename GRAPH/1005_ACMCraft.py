from heapq import heappush as push, heappop as pop
from fractions import *
T = int(input())
for _ in range(T):
    N, K = map(int,input().split())
    T = [0]+[int(i) for i in input().split()]
    edge =[[] for _ in range(N+1)]
    for _ in range(K):
        A, B = map(int, input().split())
        edge[B].append(A)
    W = int(input())

    
    accum=[-1]*(N+1)
    def heapq():
        q=[]
        push(q,(1e5-T[W], W))
        accum[W]=T[W]
        while q:
            reversed_time, building = pop(q)
            time = 1e5-reversed_time
            if accum[building]>time:
                continue
            for to in edge[building]:
                if time+T[to]> accum[to]:
                    accum[to] = accum[building]+T[to]
                    push(q, (1e5-accum[to], to))

    heapq()
    print(max(accum))

'''
2
4 4
10 1 100 10
1 2
1 3
2 4
3 4
4
8 8
10 20 1 5 8 7 1 43
1 2
1 3
2 4
2 5
3 6
5 7
6 7
7 8
7



5
3 2
1 2 3
3 2
2 1
1
4 3
5 5 5 5
1 2
1 3
2 3
4
5 10
100000 99999 99997 99994 99990
4 5
3 5
3 4
2 5
2 4
2 3
1 5
1 4
1 3
1 2
4
4 3
1 1 1 1
1 2
3 2
1 4
4
7 8
0 0 0 0 0 0 0
1 2
1 3
2 4
3 4
4 5
4 6
5 7
6 7
7
'''