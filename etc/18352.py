N, M, K, X = [int(i) for i in input().split()]
town=[]
[town.append([]) for _ in range(N+1)]
for _ in range(M):
    a, b = [int(i) for i in input().split()]
    town[a].append(b)

Q = [(X,0)]

chk=[False]*(N+1)
chk[X]=True


ans=[]
while Q:
    a = Q.pop(0)
    print(a)
    if a[1]==K:
        ans.append(a[0])
    elif a[1]>K:
        break
    for i in town[a[0]]:
        if chk[i]==False:
            chk[i]=True
            Q.append((i,a[1]+1))


if ans:
    ans.sort()
    [print(i) for i in ans]
else:
    print(-1)
'''
7 8 2 1
1 2
1 3
2 3
2 4
2 5
3 6
6 7
2 7
'''

