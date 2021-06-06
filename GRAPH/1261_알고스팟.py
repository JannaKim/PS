from heapq import heappush , heappop
n , m = map(int , input().split())
n , m = m , n
mp = [ [*map(int , list( input() )) ] for _ in range(n)]

Dy = [0 , 0 , 1 , -1]
Dx = [1 , -1 , 0 , 0]

def chk (y , x):
    if 0 <= y < n and 0 <= x < m:
        return True
    return False

W = [ [1e9] * m for _ in range(n) ]
W[0][0] = 0

q = []
heappush(q , (0 , 0 , 0))
ans = 1e9
while q:
    wall, y , x = heappop(q)
    if (y , x) == (n - 1 , m - 1):
        ans = min(ans , wall)
        continue
    if W[y][x] < wall:
        continue

    for dy , dx in zip(Dy , Dx):
        ny = y + dy
        nx = x + dx
        if chk(ny , nx) and wall+ mp[ny][nx] < W[ny][nx] :
                W[ny][nx] = wall + mp[ny][nx]
                
                heappush(q , (wall + mp[ny][nx], ny , nx))
print(ans)