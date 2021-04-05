import sys; input= lambda: sys.stdin.readline().rstrip()
from collections import deque
m, n= map(int, input().split())
box= [[*map(int, input().split())] for _ in range(n)]

Dy= [0, 0, 1, -1]
Dx= [1, -1, 0, 0]
q=deque()
for y in range(n):
    for x in range(m):
        if box[y][x]==1:
            q.append((y, x))
day=-1
while q:
    day+=1
    Len=len(q)
    for _ in range(Len):
        y, x= q.popleft()
        for dy, dx in zip(Dy, Dx):
            ny= y+dy
            nx= x+dx
            if ny>=0 and ny<n and nx>=0 and nx<m and box[ny][nx]==0:
                box[ny][nx]=1
                q.append((ny, nx))
    

for i in range(n):
    for j in range(m):
        if not box[i][j]:
            print(-1)
            exit()

print(day)
