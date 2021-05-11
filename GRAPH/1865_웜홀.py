for _ in range(int(input())):
    n, m, w= map(int, input().split())
    edge= [[] for _ in range(n+1)]
    dist= [1e10]*(n+1)
    for _ in range(m):
        s, e, t= map(int, input().split())
        if s==1:
            dist[e]= min(dist[e], t)
        if e==1:
            dist[s]= min(dist[s], t)
        edge[s].append((e, t))
        edge[e].append((s, t))
    candi=[]
    for _ in range(w):
        s, e, t= map(int, input().split())
        candi.append((s,e,-t))
        edge[s].append((e,-t))

    dist[1]= 0

    for _ in range(n):
        for v in range(1, n+1):
            for v2, w in edge[v]: 
                if dist[v2]> dist[v]+ w:
                    dist[v2]= dist[v]+ w
    #print(dist)
    flag=False
    for v in range(1, n+1):
        for v2, w in edge[v]:
            if dist[v2]> dist[v]+w:
                flag=True
                break
        if flag:
            break
    '''
    for st, ed, warf in candi:
        if dist[st]+dist[ed]+warf<0:
            #print(st,ed,warf)
            flag=True
            break
    '''
    if flag:
        print('YES')
    else:
        print('NO')

