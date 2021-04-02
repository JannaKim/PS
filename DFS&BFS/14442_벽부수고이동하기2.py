import sys; input= lambda: sys.stdin.readline().rstrip()
from collections import deque
n, m, k= map(int, input().split())
mp= [input() for _ in range(n)]

Dy= [0, 0, 1, -1]
Dx= [1, -1, 0, 0]

chk= [[-1]*m for _ in range(n)]
q= deque()
q.append((1, 0, 0, 0))
while q:
    d, y, x, crashed= q.popleft()
    if (y, x)== (n-1, m-1):
        print(d)
        exit()  
    for dy, dx in zip(Dy, Dx):
        ny= y+dy
        nx= x+dx    
        if nx<0 or nx>=m or ny<0 or ny>=n or (chk[ny][nx]>=0 and chk[ny][nx]<=crashed):
            continue
        if mp[ny][nx]=='0':
            q.append((d+1, ny, nx, crashed))
            chk[ny][nx]=crashed
        elif crashed<k: # 적게부순애가 먼저 도착했다면 갈 필요없음
            chk[ny][nx]=crashed+1
            q.append((d+1, ny, nx, crashed+1))

print(-1)


'''
6 4
0000
1110
1000
1101
1111
1100


vi example.c

테트로미노 
'''