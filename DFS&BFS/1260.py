N, M, V = [int(i) for i in input().split()]

lnk=[[] for _ in range(M)]

for _ in range(M):
    a, b = [int(i) for i in input().split()]
    lnk[a].append(b)
    lnk[b].append(a)

[a.sort() for a in lnk]
print(lnk)

'''
4 5 1
1 2
1 3
1 4
2 4
3 4

4 5 1
1 3
1 4
1 2
2 4
3 4

'''

chk = [False]*(N+1)

q = [V]
res=[]
chk[V] = True
mx=0
while q:
    a= q.pop(0)
    res.append(a)
    for v in lnk[a]:
        if chk[v]==False:
            chk[v]=True
            q.append(v)

print(res)

ck=[]
def f(a):




f(V)