# 위상 정렬: 방향성을 거스르지 않게 정점들을 나열하는 알고리즘
# indegree: 한 정점에서 자신에게 들어오는 방향인 간선의 수
# indegree 수 이용: 간선의 정보를 받을 때 indegree -=1 해주고 
# indegree=0 인 정점을 스택에 넣어준다

# 높은 서열순으로 정렬해준다.

N, E = map(int, input().split())
edge = [False]+ [[] for _ in range(N)]
indegree=[-1]+[0]*N

for _ in range(E):
    a, b = map(int, input().split())
    edge[a].append(b)
    indegree[b]+=1


def indegree_BFS():
    stack=[]
    q = [i for i in range(1,N+1) if indegree[i]==0]
    while(q):
        v = q.pop(0)
        stack.append(v)
        for v2 in edge[v]:
            indegree[v2]-=1
            if indegree[v2]==0: # 0이 아닌 애들은 나중에 다시 참조됨
                q.append(v2)
    return stack

print(edge)
print(indegree_BFS())


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



9 8
8 9
8 7
6 7
6 5
5 4
3 4
3 2
2 1
'''