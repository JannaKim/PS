
T = int(input())
for _ in range(T):
    N, K = map(int,input().split())
    T = [0]+[int(i) for i in input().split()]
    edge =[[] for _ in range(N+1)]

    for _ in range(K):
        A, B = map(int, input().split())
        edge[B].append(A)
        
    W = int(input())

    
    q = [(T[W],W)]
    accum = [-1]*(N+1)
    accum[W] = T[W]
    while q:
        tmp, v = q.pop(0)
        if tmp<accum[v]:
            continue
        for v2 in edge[v]:
            if accum[v2]< tmp+T[v2]:
                accum[v2] = tmp+T[v2]
                q.append((accum[v2],v2))

   
    print(max(accum[1:]))


'''
1
4 4
10 1 100 10
1 2
1 3
2 4
3 4
4
'''
    

