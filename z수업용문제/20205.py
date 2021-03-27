n, k= map(int, input().split())
ori= []
for i in range(n):
    ori.append([*map(int, input().split())])

for i in range(n):
    L=[]
    for j in range(n):
        for _ in range(k):
            L.append(ori[i][j])
    for _ in range(k):
        print(*L)    


    