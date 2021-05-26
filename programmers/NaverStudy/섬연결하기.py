par= []
def find(v):
    if par[v]==v:
        return v
    else:
        par[v]=find(par[v])
        return par[v]
def union(u,v):
    r1=find(u)
    r2=find(v)
    if r1<r2:
        par[r2]=r1
    else:
        par[r1]=r2
def solution(n, costs):
    global par
    par= list(range(n))
    ans = 0
    costs.sort(key= lambda x:x[2])

    for a, b, c in costs:
        par[a]=find(a)
        par[b]=find(b)
        if par[a]!=par[b]:
            ans+=c
            union(a,b)
    return ans


#print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))
#print(solution(5, [[0,1,1],[0,2,1],[0,3,1],[0,4,1],[1,2,100],[2,3,100],[3,4,100]]))
#print(solution(4, [[0,1,1],[0,2,1],[1,2,5],[1,3,1],[2,3,1]]))
print(solution(5, [[0,1,5],[1,2,3],[2,3,3],[3,1,2],[3,0,4],[2,4,6],[4,0,7]]))
