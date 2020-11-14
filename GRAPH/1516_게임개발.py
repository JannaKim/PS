N = int(input())
edge = [False] + [[] for _ in range(N)]
dur = [-1]*(N+1)
for i in range(1,N+1):
    L = [int(i) for i in input().split()]
    dur[i] = L[0]
    if L[1:-1]:
        for v2 in L[1:-1]:
            edge[i].append(v2)

accum= [False]+[-1]*N

def Pseudo_Dijik(v):
    q=[]
    q.append((v,dur[v]))
    accum[v] = dur[v]
    while q:
        v, tmp = q.pop(0)
        if tmp<accum[v]:
            continue
        for v2 in edge[v]:
            if dur[v2]+tmp>accum[v2]:
                accum[v2] = dur[v2]+tmp
                q.append((v2, accum[v2]))
    

for i in range(1,N+1):
    accum= [False]+[-1]*N
    Pseudo_Dijik(i)
    print(max(accum))

'''
5
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1
'''
    

