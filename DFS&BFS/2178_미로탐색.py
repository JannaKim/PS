from heapq import heappush, heappop
import sys; input= lambda: sys.stdin.readline().rstrip()
n, m= map(int, input().split())

mp= [[-1]*(m+2)]

for _ in range(n):
    mp += [[-1]+list(map(int, list(input())))+ [-1]]

mp+= [[-1]*(m+2)]

q= []
heappush(q, (1, 1, 1))
Dy= [-1, 0, 0, 1]
Dx= [0, 1, -1, 0]
chk= [[False]*(m+2) for _ in range(n+2)]
while q:
    d, y, x= heappop(q)
    if (y, x) == (n, m):
        print(d)
        exit()

    

    for dy, dx in zip(Dy, Dx):
        ny= y+ dy
        nx= x+ dx
        if mp[ny][nx]==1 and not chk[ny][nx]: # 같은곳을 같이 바라보는 애들 때문에 문제됨
            chk[ny][nx]=True
            heappush(q,(d+1, ny, nx))