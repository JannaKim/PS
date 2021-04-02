import sys; input= lambda: sys.stdin.readline().rstrip()
from heapq import heappop, heappush
for _ in range(int(input())):
    n= int(input())
    edge=[[] for _ in range(n+1)]
    up=[[] for _ in range(n+1)]
    indegree= [True]*(n+1)
    for _ in range(n-1):
        a, b= map(int, input().split())
        edge[a].append(b)
        up[b].append(a)
        indegree[b]=False

    # 둘을 이은다음에 bfs, 만나면 그중에 공통조상 있다.

    def fill_story(v,floor):
        for v2 in edge[v]:
            story[v2]= min(story[v2], floor+1)
            fill_story(v2,floor+1)


    story= [1e9]*(n+1)
    for i in range(1,n+1):
        if indegree[i]:
            indegree=[]
            story[i]=0
            fill_story(i,0)
            edge=[]
            break

    chk= [False]*(n+1)
    a, b= map(int, input().split())
    q=[]
    chk[a]=True
    chk[b]=True
    heappush(q, (-story[a], a))
    heappush(q, (-story[b], b))

    while q:
        stry, v= heappop(q)
        #print(-stry, v)
        found=False
        for v2 in up[v]:
            #print(v, '->', v2, -stry)
            if not chk[v2]:
                chk[v2]=True
                heappush(q, (-story[v2], v2))
            else:
                found=True
                break
        if found:
            q=[]
            break
    
    ans=-1
    mn=1e9
    #print(chk)
    #print(story)
    for i in range(1,n+1):
        if chk[i] and story[i]<mn:
            ans=i
            mn=story[i]
    print(ans)


