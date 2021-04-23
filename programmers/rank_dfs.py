def solution(n, results):
    answer = 0
    edge= [[] for _ in range(n+1)]
    indegree=[0]*(n+1)
    m= len(results)
    for a, b in results:
        edge[a].append(b)
        indegree[b]+=1

    rank=[0]*(n+1)
    dep=[0]*(n+1)
    print(indegree)
    def dfs(v):
        print(v)
        for v2 in edge[v]:
            print('->', v2)
            indegree[v2]-=1
            if not indegree[v2]:
                dep[v2]= max(dep[v2], dep[v]+1)
                print(dep)

    for i in range(1,n+1):
        if not indegree[i]:
            dfs(i)
    print(dep)

print(solution(7,[[1,2], [1,3], [1,4], [7,4], [2,5], [3,5], [4,5], [5,6], [4,3]]))