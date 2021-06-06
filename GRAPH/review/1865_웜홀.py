tc = int(input())
for _ in range(tc):
    n , m , w = map(int, input().split())
    edge = [ [] for _ in range(n+1)]
    dist = [1e10] * (n + 1)
    for _ in range(m):
        s , e , t = map(int, input().split())
        edge[s].append( (e , t))
        edge[e].append( (s , t))

    for _ in range(w):
        s , e , t = map(int, input().split())
        edge[s].append( (e , -t))

    for _ in range(n - 1):
        for v in range(1, n+1):
            for v2, w in edge[v]: 
                if dist[v2]> dist[v]+ w:
                    dist[v2]= dist[v]+ w
    flag=False
    for v in range(1, n+1):
        for v2, w in edge[v]:
            if dist[v2]> dist[v]+w:
                flag=True
                break
        if flag:
            break
    
    if flag:
        print('YES')
    else:
        print('NO')
