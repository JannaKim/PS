import sys
n, m, K= map(int, input().split())

food= [[*map(int, sys.stdin.readline().rstrip().split())] for _ in range(n)]
tree=[[{} for _ in range(n)] for _ in range(n)]
for _ in range(m):
    a, b, c= map(int, sys.stdin.readline().rstrip().split())
    tree[a-1][b-1][c]=1

forest= [[5]*n for _ in range(n)]
Dy= [0,0,1,1,1,-1,-1,-1]
Dx= [1,-1,1,-1,0,1,-1,0]

for k in range(K):
    breed=[]
    for i in range(n):
        for j in range(n):
            if not tree[i][j]:
                forest[i][j]+=food[i][j]
                continue
            info=sorted(tree[i][j].items())
            tree[i][j].clear()
            deadNour=0
            for lev, amnt in info:
                levUps=min(forest[i][j]//lev,amnt)
                if levUps:
                    if not (lev+1)%5:
                        breed.append((i,j,levUps))
                    forest[i][j]-=levUps*lev
                    tree[i][j][lev+1]=levUps

                deadNour+=(amnt-levUps)*(lev>>1)
            forest[i][j]+=deadNour+food[i][j]

    for y, x, amnt in breed:
        for dy, dx in zip(Dy, Dx):
            ny, nx= y+dy,x+dx
            if 0<=ny<n and 0<=nx<n:
                tree[ny][nx][1]=tree[ny][nx].get(1,0)+amnt

#print(sum(sum(tree[i//n][i % n].values()) for i in range(n**2)))
ans=0
for i in range(n):
    for j in range(n):
        ans+=sum(tree[i][j].values())
print(ans)