import sys; input= lambda: sys.stdin.readline().rstrip()
forward= [(-1, 0), (0, -1), (1, 0), (0, 1)]
backward= [(1, 0), (0, 1), (-1, 0), (0, -1)]

n, m= map(int, input().split())
r, c, d= map(int, input().split())
if d==1:
    d=3
elif d==3:
    d=1
floor= [[*map(int, input().split())] for _ in range(n)]

ans=1
def clean(y, x, d):
    global ans
    flag=False
    for _ in range(4):
        d= (d+1)%4
        ny= y+forward[d][0]
        nx= x+forward[d][1]
        if nx<0 or nx>=m or ny<0 or ny>=n or floor[ny][nx]>=1:
            continue
        flag=True
        floor[ny][nx]=2
        ans+=1
        clean(ny, nx, d)
        break
    if not flag:
        ny= y+backward[d][0]
        nx= x+backward[d][1]
        if nx<0 or nx>=m or ny<0 or ny>=n or floor[ny][nx]==1:
            print(ans)
            exit()
        clean(ny, nx, d)
floor[r][c]=2
clean(r, c, d)

# bfs 로 해보기