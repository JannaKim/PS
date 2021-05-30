import sys
n, m, K= map(int, input().split())

food= [[*map(int, sys.stdin.readline().rstrip().split())] for _ in range(n)]
tree=[[{} for _ in range(n)] for _ in range(n)]
for _ in range(m):
    a, b, c= map(int, sys.stdin.readline().rstrip().split())
    tree[a-1][b-1][c]=1

forest= [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        forest[i][j]=5-food[i][j]
Dy= [0,0,1,1,1,-1,-1,-1]
Dx= [1,-1,1,-1,0,1,-1,0]

for k in range(K):
    breed=[]
    for i in range(n):
        for j in range(n):
            forest[i][j]+=food[i][j] # if문 지우고 n*n 추가했더니 빨라짐
            info= sorted(tree[i][j].items())
            if not info: continue
            tree[i][j].clear()
            deadNour=0
            for lev, amnt in info:
                levUps=min(forest[i][j]//lev,amnt)
                if levUps:
                    if not (lev+1)%5:
                        breed.append((i,j,levUps))
                    forest[i][j]-=levUps*lev
                    tree[i][j][lev+1]=levUps

                deadNour+=(amnt-levUps)*(lev//2)
            forest[i][j]+=deadNour

    for y, x, amnt in breed:
        for dy, dx in zip(Dy, Dx):
            ny, nx= y+dy,x+dx
            if 0<=ny<n and 0<=nx<n:
                if 1 not in tree[ny][nx]:
                    tree[ny][nx][1]=0
                tree[ny][nx][1]+=amnt

ans=0
for i in range(n):
    for j in range(n):
        ans+=sum(tree[i][j].values())
print(ans)