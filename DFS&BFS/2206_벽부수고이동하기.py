import sys; input= lambda: sys.stdin.readline().rstrip()
#from heapq import heappush, heappop
from collections import deque
n, m= map(int, input().split())
mp= [[-1]*(m+2)]
mp+= [[-1]+list(map(int, list(input())))+ [-1] for _ in range(n)]
mp+=[[-1]*(m+2)]


#[print(*el) for el in mp]
Dy= [0, 0, 1, -1]
Dx= [1, -1, 0, 0]

chk= [[False]*(m+2) for _ in range(n+2)]
chk2= [[False]*(m+2) for _ in range(n+2)]
ans= 1e9
q= deque()
q.append((1, 1, 1, False))
while q:
    d, y, x, crashed= q.popleft()
    if (y, x)== (n, m):
        ans= min(ans, d)
    
    for dy, dx in zip(Dy, Dx):
        ny= y+dy
        nx= x+dx
        if crashed:
            if chk2[ny][nx] or mp[ny][nx]<0:
                continue
            if mp[ny][nx]==0:
                chk2[ny][nx]=True
                q.append((d+1, ny, nx, crashed))
        else: # not crashed
            if chk[ny][nx] or mp[ny][nx]<0:
                continue

            if mp[ny][nx]==1:
                chk[ny][nx]= True
                q.append((d+1, ny, nx, True))
            elif mp[ny][nx]==0:
                chk[ny][nx]= True
                q.append((d+1, ny, nx, crashed))


print([ans, -1][ans==1e9])


'''
6 4
0000
1110
1000
1101
1111
1100
'''