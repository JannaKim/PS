n, e= map(int, input().split())
edge=[[] for _ in range(n+1)]
for _ in range(e):
    a, b= map(int, input().split())
    edge[a].append(b)

bundle=[]
b=0
visited=[0]*(n+1) # 정점들에 번호매김
where= [0]*(n+1)
cur=0
q=[]
def scc(v):
    global cur, b
    cur+=1
    visited[v]=cur
    ret= visited[v]
    q.append(v)

    for v2 in edge[v]:
        if not visited[v2]:
            ret= min(ret, scc(v2))
        elif not where[v2]: # 방문은했는데 scc로 안묶임
            ret= min(ret, visited[v2]) # 그중 가장 작은 번호찾기
    
    if ret==visited[v]:
        tmp=[]
        while True:
            ths= q.pop()
            where[ths]=b
            b+=1
            tmp.append(ths)
            if ths==v:
                break
        bundle.append(sorted(tmp))
    return ret

for i in range(1,n+1):
    if not visited[i]:
        scc(i)

print(len(bundle))
bundle.sort()
for el in bundle:
    print(*el, end=' ')
    print(-1)




