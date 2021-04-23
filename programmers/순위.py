
def solution(n, results):
    answer = 0
    edge= [[] for _ in range(n+1)]
    indegree=[0]*(n+1)
    edge2= [[] for _ in range(n+1)]
    indegree2= [0]*(n+1)
    m= len(results)
    for a, b in results:
        edge[a].append(b)
        indegree[b]+=1
        edge2[b].append(a)
        indegree2[a]+=1
        
    up=[0]*(n+1)
    down=[0]*(n+1)
    for i in range(1,n+1):
        up[i]=set()
        down[i]=set()
    
    def rate(v):
        #print(v,up[v])
        for v2 in edge[v]:
            up[v2].update(list(up[v]))
            up[v2].add(v)
            rate(v2)
    def rate2(v):
        for v2 in edge2[v]:
            down[v2].update(list(down[v]))
            down[v2].add(v)
            rate2(v2)
    #print(indegree)
    for i in range(1,n+1):
        if not indegree[i]:
            #print('zero')
            rate(i)
        if not indegree2[i]:
            rate2(i)
    for i in range(1,n+1):
        #print(up[i], down[i])
        if len(up[i])+len(down[i])==n-1:
            answer+=1
    return answer