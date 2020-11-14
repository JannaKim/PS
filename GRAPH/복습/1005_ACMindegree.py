# 두가지 길이 하나로 모아졌을 때 좋지 않은 길이 계산되면 시간낭비다
# indegree를 원하는 상황에 맞춰 넣을 수가 없다.

# 원하는 W 의 자식노드들만 indegree를 설정해야 한다.
# 모든 building이 아닌, 원하는 building을 짓는 데 걸리는 시간을 요구한다
# indegree 계산 따로 해주는 함수 때문에 시간초과
T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    edge = [False]+[[] for _ in range(N)]
    D = [0] + [int(i) for i in input().split()]
    indegree = [-1]+[0]*N

    for _ in range(K): #간선 저장
        a, b = map(int, input().split())
        edge[b].append(a)
        #indegree[a]+=1
    W = int(input())

    def set_indegree(W):
        q = [W]
        while q:
            v = q.pop(0)
            for v2 in edge[v]:
                indegree[v2]+=1
                q.append(v2)

    accum = [-1]*(N+1)
    
    def indegree_BFS(): # 위상정렬
        q = []
        q.append(W)
        accum[W] = D[W]
        while q:
            v = q.pop(0)
            print('v= ',v)
            for v2 in edge[v]:
                print('v2',v2)
                indegree[v2]-=1
                print(f'accum[{v2}], accum[{v}]+D[{v2}]')
                print(f'{accum[v2]}, {accum[v]}+{D[v2]}')
                accum[v2] = max(accum[v2],accum[v]+D[v2])
                if indegree[v2]==0: # dur[v2]가 최대시간으로 고정됨
                    q.append(v2) # 고정된 dur[v2]만을 q에 push
    print(edge)
    
    print(D)
    set_indegree(W)
    print(indegree)
    indegree_BFS()
    print(accum)
    print(max(accum[1:]))

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
