r, c= map(int, input().split())
k= int(input())

grid= [[-1]*(c+2)]
grid+= [[-1]+[0]*c+[-1] for _ in range(r)]
grid+=[[-1]*(c+2)]
dy=[0,1,0,-1]
dx=[1,0,-1,0]

d=0

if k>r*c:
    print(0)
    exit()
y=1
x=0

for i in range(1,k+1):
    if grid[y+dy[d]][x+dx[d]]:
        d=(d+1)%4
    y=y+dy[d]
    x=x+dx[d]
    grid[y][x]=i
    #[print(*el) for el in grid]
    if i==k:
        print(y,x)
