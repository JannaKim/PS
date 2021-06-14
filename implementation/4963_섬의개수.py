
from collections import deque
Dy = [0,0,   1,1,1,  -1,-1,-1]
Dx = [1,-1,  1,-1,0,  1,-1,0]
chk = []
mp = []
h , w = -1, -1
def valid(y , x):
    if y < 0 or y >= h or x < 0 or x >= w:
        return False
    if chk[y][x]:
        return False
    if not mp[y][x]:
        return False
    return True
def bfs(chk, y , x):
    q = deque()
    q.append( (y, x))
    while q:
        y , x  = q.popleft()
        for dy , dx in zip(Dy , Dx):
            ny = y + dy
            nx = x + dx
            if valid(ny , nx):
                chk[ny][nx] = True
                q.append( (ny , nx))

while True:
    w , h = map(int, input().split())
    if not w * h:
        break
    mp = [ [*map(int, input().split())] for _ in range(h)]
    chk = [ [False] * w for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if mp[i][j] and not chk[i][j]:
                chk[i][j] = True
                cnt += 1
                bfs(chk , i , j)
    print(cnt)
                