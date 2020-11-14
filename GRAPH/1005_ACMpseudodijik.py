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
        q.append((T[W], W))
        accum[W]=T[W]
        while q:
            time, v = q.pop(0)
            if accum[v]>time:
                continue
            for v2 in edge[v]:
                if time+T[v2]> accum[v2]:
                    accum[to] = accum[v]+T[v2]
                    q.append((accum[v2], v2))

    heapq()
    print(max(accum))