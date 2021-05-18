import sys; input= lambda: sys.stdin.readline().rstrip()
from collections import deque
n, m, k= map(int, input().split())
food=[]
for _ in range(n):
    food.append([*map(int, input().split())])
tree=[[[0,deque()] for _ in range(n)] for _ in range(n)]
alive=set()
for _ in range(m):
    a, b, c= map(int, input().split())
    a-=1
    b-=1
    tree[a][b][0]+=1
    tree[a][b][1].append(c)
    alive.add((a,b))

forest= [[5]*n for _ in range(n)]
Dy= [0,0,1,1,1,-1,-1,-1]
Dx= [1,-1,1,-1,0,1,-1,0]
ans=m
for t in range(k):
    spread=[]
    dead=set()
    for (i,j) in alive:
        cnt=0
        for k in range(tree[i][j][0]-1,-1,-1):

            if forest[i][j]+food[i][j]*t>=tree[i][j][1][k]:
                forest[i][j]-=tree[i][j][1][k]
                tree[i][j][1][k]+=1
                if not tree[i][j][1][k]%5:
                    spread.append((i,j))
            else:
                cnt=k+1
                break
        for _ in range(cnt):
            tree[i][j][0]-=1
            forest[i][j]+=(tree[i][j][1].popleft()//2)
        
            if not tree[i][j][0]:
                dead.add((i,j))
        ans-=cnt
    alive-=dead

    for y, x, in spread:
        for dy, dx in zip(Dy, Dx):
            ny, nx= y+dy,x+dx
            if 0<=ny<n and 0<=nx<n:
                tree[ny][nx][0]+=1
                tree[ny][nx][1].append(1)
                alive.add((ny,nx))
                ans+=1

print(ans)


'''
10 100 1000
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
1 1 4
1 2 4
1 3 4
1 4 4
1 5 4
1 6 4
1 7 4
1 8 4
1 9 4
1 10 4
2 1 4
2 2 4
2 3 4
2 4 4
2 5 4
2 6 4
2 7 4
2 8 4
2 9 4
2 10 4
3 1 4
3 2 4
3 3 4
3 4 4
3 5 4
3 6 4
3 7 4
3 8 4
3 9 4
3 10 4
4 1 4
4 2 4
4 3 4
4 4 4
4 5 4
4 6 4
4 7 4
4 8 4
4 9 4
4 10 4
5 1 4
5 2 4
5 3 4
5 4 4
5 5 4
5 6 4
5 7 4
5 8 4
5 9 4
5 10 4
6 1 4
6 2 4
6 3 4
6 4 4
6 5 4
6 6 4
6 7 4
6 8 4
6 9 4
6 10 4
7 1 4
7 2 4
7 3 4
7 4 4
7 5 4
7 6 4
7 7 4
7 8 4
7 9 4
7 10 4
8 1 4
8 2 4
8 3 4
8 4 4
8 5 4
8 6 4
8 7 4
8 8 4
8 9 4
8 10 4
9 1 4
9 2 4
9 3 4
9 4 4
9 5 4
9 6 4
9 7 4
9 8 4
9 9 4
9 10 4
10 1 4
10 2 4
10 3 4
10 4 4
10 5 4
10 6 4
10 7 4
10 8 4
10 9 4
10 10 4


'''