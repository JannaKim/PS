# 위상 정렬: 방향성을 거스르지 않게 정점들을 나열하는 알고리즘
# DFS Spanning Tree: visited 이용

# DFS로 모든 방향성을 거스르지 않고 정렬한다는게 말이 안된다
N, E = map(int, input().split())
edge = [False]+ [[] for _ in range(N)]
for _ in range(E):
    a, b = map(int, input().split())
    edge[a].append(b)

visited = [True] + [False]*N
def DFS(v):
    global edge
    global visited
    visited[v] = True
    for v2 in edge[v]:
        if visited[v2]==False:
            DFS(v2)
    print(v,end=' ')

for i in range(1,N+1):
    if visited[i]==False:
        DFS(i)

'''
12 13
1 2
1 3
1 4
2 6
2 9
6 5
6 7
5 8
9 8
7 10
7 11
9 12
10 12

7 9
4 2
6 2
6 4
3 7
1 3
1 5
1 7
7 6
5 6
'''