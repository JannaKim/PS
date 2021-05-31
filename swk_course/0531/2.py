from heapq import heappop, heappush


for _ in range(int(input())):
    m= int(input())
    st= tuple(map(int, input().split()))
    accum= {}
    accum[st]=0
    conv=[]
    for _ in range(m):
        a,b= map(int, input().split())
        conv.append((a,b))
        accum[(a,b)]=1e9
    dest= tuple(map(int, input().split()))
    accum[dest]=1e9

    #print(accum)
    L=[st]+conv[:]+[dest]
    #print(L)
    edge={}
    for i in range(m+2-1):
        for j in range(i+1,m+2):
            y1, x1= L[i]
            y2, x2= L[j]
            #print(L[i], L[j])
            #print(abs(y1-y2)+abs(x1-x2))
            if (abs(y1-y2)+abs(x1-x2)+49)//50<=20:
                if (y1,x1) not in edge:
                    edge[(y1,x1)]=[]
                edge[(y1,x1)].append((y2,x2))

                if (y2,x2) not in edge:
                    edge[(y2,x2)]=[]
                edge[(y2,x2)].append((y1,x1))

    #print(edge)
    q=[]
    heappush(q,(st,0))
    while q:
        v, c= heappop(q)
        #print(v,c)
        if c<accum[v]:
            continue
        if v not in edge:
            continue
        for v2 in edge[v]:
            if c+1<accum[v2]:
                accum[v2]=c+1
                heappush(q,(v2,accum[v2]))
    
    if accum[dest]<1e9:
        print('happy')
    else:
        print('sad')


'''
1
2
0 0
1000 0
1000 1000
2000 1000
'''