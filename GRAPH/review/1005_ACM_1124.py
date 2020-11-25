from collections import deque

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    D =[0] + list(map(int, input().split()))
    edge = [[] for _ in range(N+1)]
    for _ in range(K):
        a, b = map(int, input().split())
        edge[b].append(a)
    X = int(input())
    store = [-1]*(N+1)
    store[X] = D[X]
    def pseudo_dijik():
        Q = deque()
        Q.append((X, D[X]))


        while Q:
            v, t = Q.popleft()

            if store[v]>t:
                if not Q: break
                v, t = Q.popleft()

            for v2 in edge[v]:
                if D[v2]+t>store[v2]: 
                    store[v2]= D[v2]+t
                    Q.append((v2,store[v2])) 

    pseudo_dijik()
    print(max(store))

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
'''


