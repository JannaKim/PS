N, M, V = [int(i) for i in input().split()]
v=[]
[v.append([]) for _ in range(N+1)]

for _ in range(M):
    e1, e2 = [int(i) for i in input().split()]
    v[e1].append(e2)
    v[e2].append(e1)


[info.sort() for info in v]

dic={}
# [dic[i]=False for i in range(1,N+1)]

for i in range(1,N+1):
    dic[i]=False

def f(idx):
    dic[idx]=True
    print(idx,end=' ')
    for i in v[idx]:
        if dic[i]==False:
            f(i)

f(V)


print()

q=[V]
dic={}
# [dic[i]=False for i in range(1,N+1)]

for i in range(1,N+1):
    dic[i]=False

dic[V] = True
while q:
    idx = q.pop(0)
    print(idx, end=' ')
    for i in v[idx]:
        if dic[i]==False:
            dic[i] = True
            q.append(i)





'''
4 5 1
1 2
1 3
1 4
2 4
3 4

5 5 3
5 4
5 2
1 2
3 4
3 1
'''
