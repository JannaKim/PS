from heapq import heappush as push, heappop as pop
V, E = map(int,input().split())
K = int(input())
fromto=[[] for i in range(V+1)]
for _ in range(E):
    u, v, w = [int(i) for i in input().split()]
    fromto[u].append((w,v))

mindist=[2e9]*(V+1)

def heapq(start):
    global mindist
    w, v=start
    mindist[v]=w
    q=[]
    push(q,(w,v))

    while q:
        w, v = pop(q)
        if mindist[v]<w:
            continue
        for given_w, to in fromto[v]:
            if mindist[to]>given_w+ w:
                mindist[to]=given_w+ w
                push(q,(mindist[to], to))

heapq((0,K))
[print('INF' if i==2e9 else i) for i in mindist[1:]]

    


'''
5 6
1
5 1 1
1 2 2
1 3 3
2 3 4
2 4 5
3 4 6

'''