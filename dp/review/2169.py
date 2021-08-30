import sys; sys.setrecursionlimit(100000)
n, m = map(int, input().split())
mp = [ [*map(int, input().split())] for _ in range(n)]

Dy= [0, -1, 0] # 왼, 위, 오
Dx= [-1, 0, 1]
dp= [[[-1e9] * m for _ in range(n)] for _ in range(3)]

def bound(y, x):
    if y < 0 or y >= n:
        return False
    if x < 0 or x >= m:
        return False
    return True

def topdown(y, x, dir):
    if (y, x) == (0, 0):
        return mp[y][x]
    if dp[dir][y][x] != -1e9:
        return dp[dir][y][x]
    mx = -1e9
    for d, (dy, dx) in enumerate( zip(Dy, Dx) ):
        if abs(d - dir) == 2 and dir != -1:
            continue
        ny = y + dy
        nx = x + dx
        if not bound(ny, nx):
            continue
        mx = max(mx, topdown(ny, nx, d))
    dp[dir][y][x]= mx + mp[y][x]
    return dp[dir][y][x]


print(topdown(n-1, m-1, -1))