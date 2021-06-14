import sys; sys.setrecursionlimit(250*2000 + 1)
input= lambda: sys.stdin.readline().strip()
n , L , R = map(int, input().split())
mp = [ [*map(int, input().split())] for _ in range(n)]

Dy = [0,1,0,-1]
Dx = [1,0,-1,0]

def bound(y, x):
    if 0 <= y < n and 0 <= x < n:
        return True
    return False

def allowed(y , x , ny , nx):
    global L , R
    if L <= abs(mp[y][x] - mp[ny][nx]) <= R:
        return True
    return False


for t in range(2001):
    dp = [ [[False]*4 for _ in range(n)] for __ in range(n)]

    def connect(y , x , ay , ax):
        for idx , (dy , dx) in enumerate(zip(Dy , Dx)):
            ny , nx = y + dy , x + dx
            if bound(ny,nx) and (ny,nx) == (ay,ax):
                dp[y][x][idx] = True

        for idx , (dy , dx) in enumerate(zip(Dy , Dx)):
            ny , nx = ay + dy , ax + dx
            if bound(ny,nx) and (ny,nx) == (y,x):
                dp[ay][ax][idx] = True

    for y in range(n):
        for x in range(n):
            for dy , dx in zip(Dy , Dx):
                ny = y + dy
                nx = x + dx
                if bound(ny , nx) and allowed(y ,x ,ny,  nx):
                    connect(y , x , ny, nx)

    chk = [[False]*n for _ in range(n)]
    def dfs(y,  x):
        stc = [(y , x)]
        sm = mp[y][x]
        for idx , (dy , dx) in enumerate(zip(Dy , Dx)):
            ny , nx = y + dy , x + dx
            if bound(ny,nx) and dp[y][x][idx] and not chk[ny][nx]:
                chk[ny][nx] = True
                tmp = dfs(ny, nx)
                stc += tmp[0][:]
                sm += tmp[1]

        return [stc , sm]
    nxt = False
    for i in range(n):
        for j in range(n):
            if not chk[i][j]:
                chk[i][j] = True
                tmp = dfs(i,j)
                countries = len(tmp[0])
                if countries>1:
                    nxt = True
                    balance = tmp[1]//countries
                    for y,  x in tmp[0]:
                        mp[y][x] = balance
    if not nxt:
        print(t)
        break



