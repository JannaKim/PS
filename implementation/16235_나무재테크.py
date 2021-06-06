import sys; input= lambda: sys.stdin.readline().rstrip()
n, m, K= map(int, input().split())
food=[]
for _ in range(n):
    food.append([*map(int, input().split())])
tree=[[[0 for __ in range(1011)] for _ in range(n)] for _ in range(n)]
alive=set()
for _ in range(m):
    a, b, c= map(int, input().split())
    a-=1
    b-=1
    tree[a][b][c]+=1
    alive.add((a,b))

forest= [[5 for __ in range(n)] for _ in range(n)]
Dy= [0,0,1,1,1,-1,-1,-1]
Dx= [1,-1,1,-1,0,1,-1,0]

for t in range(K):
    grown=[]
    spread={}
    dead={}
    for loc in alive:
        i,j= loc
        cnt=0
        isEmpty=True
        for k in range(1,1011):
            if tree[i][j][k]==0:
                continue
            able=0
            if (forest[i][j]+food[i][j]*t)>0:
                able= (forest[i][j]+food[i][j]*t)//k
            survived=1e9
            survived= min(able, tree[i][j][k])
            
            if survived>0:
                isEmpty= False
                forest[i][j]-=survived*k
                grown.append((i,j,k+1,survived))
                if not (k+1)%5:
                    if (i,j) not in spread:
                        spread[(i,j)]=0
                    spread[(i,j)]+=survived
            d= tree[i][j][k]-survived
            if d>0:
                if (i,j) not in dead:
                    dead[(i,j)]=0
                dead[(i,j)]+=(k//2)*d # found!
            tree[i][j][k]=0
        if isEmpty:
            alive-=set((i,j))
    #print(grown, dead, spread)
    for y, x, age, amount in grown:
        tree[y][x][age]+=amount
    for k, v in dead.items():
        y,x= k
        forest[y][x]+=v
    for loc , v in spread.items():
        y, x= loc
        for dy, dx in zip(Dy, Dx):
            ny, nx= y+dy,x+dx
            if 0<=ny<n and 0<=nx<n:
                tree[ny][nx][1]+=v
                alive.add((ny,nx))
ans=0
for i in range(n):
    for j in range(n):
        ans+=sum(tree[i][j])
print(ans)


'''
10 10 1000
100 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1
2 2 1
3 3 1
4 4 1
5 5 1
6 6 1
7 7 1
8 8 1
9 9 1
10 10 1


10 1 1000
100 100 100 100 100 100 100 100 100 100
100 100 100 100 100 100 100 100 100 100
100 100 100 100 100 100 100 100 100 100
100 100 100 100 100 100 100 100 100 100
100 100 100 100 100 100 100 100 100 100
100 100 100 100 100 100 100 100 100 100
100 100 100 100 100 100 100 100 100 100
100 100 100 100 100 100 100 100 100 100
100 100 100 100 100 100 100 100 100 100
100 100 100 100 100 100 100 100 100 100
1 1 1

log10000 1000만 1.3억

100 000 000

1억
'''