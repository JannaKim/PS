
ans=1e9
def solution(n, start, end, roads, traps):
    global ans
    ted= [False]*(n+1)
    switch= [0]*(n+1)
    edge=[[[0 for __ in range(2)] for _ in range(n+1)] for _ in range(n+1)]
    for a, b, c in roads:
        edge[a][b]=[c,1]
        edge[b][a]=[c,-1]

    for el in traps:
        ted[el]=True

    def dfs(v, cost, end,dep):
        [print(*el) for el in edge]
        print(' '*dep,v, cost)
        global ans
        if v==end:
            ans= min(ans, cost)
            return

        if ted[v]:
            for i in range(1,n+1):
                print(' '*dep,'cur',i, edge[v][i][1])
                if edge[v][i][1]:
                    ori= edge[i][v][1]
                    edge[i][v][1]=-ori
                    edge[v][i][1]=ori
                    if edge[v][i][1]==1:
                        switch[v]+=1
                        if switch[v]>2:
                            switch[v]-=1
                            continue
                        dfs(i,cost+edge[v][i][0],end,dep+1)
                        switch[v]-=1
                    edge[i][v][1]=ori
                    edge[v][i][1]=-ori
        else:
            for i in range(1,n+1):
                if edge[v][i][1]==1:
                    switch[v]+=1
                    if switch[v]>2:
                        switch[v]-=1
                        continue
                    dfs(i,cost+edge[v][i][0],end,dep+1)
                    switch[v]-=1

            





    switch[start]=1
    dfs(start,0,end,0)

    return ans