n = int(input())
k = int(input())
Dy = [0, 1, 0, -1] # 오아왼위
Dx = [1, 0, -1, 0]
dir  =0
mp = [[0]*n for _ in range(n)]
chk = [ [-1]*n for _ in range(n)]
ans = 0
ty, tx, hy, hx = 0, 0, 0, 0
chk[hy][hx] = 0
def bound(y, x):
    if y<0 or y>=n or x<0 or x>=n:
        return False
    if chk[y][x]!=-1:
        return False
    return True

def movetail(y, x):
    global ty, tx
    for dy, dx in zip(Dy, Dx):
        if 0 <= y + dy< n and 0 <= x + dx< n and chk[y + dy][x + dx] -1 == chk[y][x]:
            chk[y][x] = -1
            ty, tx = y + dy, x + dx
            return

timeinfo = [0]* 10001
def move():
    global dir, ans, hy, hx, ty, tx
    ans += 1
    hy += Dy[dir]
    hx += Dx[dir]
    if not bound(hy, hx):
        return False
    chk[hy][hx] = ans
    if not mp[hy][hx]:
        movetail(ty, tx)
    else:
        mp[hy][hx] = 0
    #print(*chk, sep='\n')
    #print(ty ,tx)
    if timeinfo[ans]:
        dir = (dir + timeinfo[ans]) % 4
    return True
for _ in range(k):
    a, b = map(int, input().split())
    mp[a-1][b-1] = 1

D={"D":1, "L":-1}
l = int(input())


for _ in range(l):
    time, d = input().split()
    time = int(time)
    timeinfo[time] = D[d]

while True:
    if not move():
        break
print(ans)


'''
5
0
5
4 D
8 D
12 D
15 D
20 L

8
3
5 4
5 8
2 5
6
7 D
11 D
15 D
18 D
19 D
20 D
'''