# TLE
import sys; input= lambda: sys.stdin.readline().rstrip()
#rom heapq import heappush, heappop
from collections import deque
n, m= map(int, input().split())
mars=[[*map(int, input().split())] for _ in range(n)]

Dy= [0,1,0]
Dx= [1,0,-1]

q=deque()
#heappush(q,(-mars[0][0]-mars[0][1], 0, 1,0,1))
#heappush(q,(-mars[0][0]-mars[1][0], 1, 0,1,1))
q.append((-mars[0][0]-mars[0][1], 0, 1,0,1))
q.append((-mars[0][0]-mars[1][0], 1, 0,1,1))
dp= [[[-1e9]*m for _ in range(n)] for _ in range(3)]
#chk= [[[False]*m for _ in range(n)] for _ in range(3)]
#for i in range(3):
#    chk[i][0][0]=True
ans=-1e9
#walks=[-1e9]*(n**2)
while q:
    cost, y, x,d,w= q.popleft()
    #print(cost,y,x,d)
    cost=-cost
    if y==n-1 and x==m-1:
        ans=max(ans,cost)
        continue
    if dp[d][y][x]>cost or dp[1][y][x]>cost:
        continue
    for dir, (dy, dx) in enumerate(zip(Dy, Dx)):
        if 2-dir==d:
            continue
        ny= y+dy
        nx= x+dx
        if 0<=nx and nx<m and 0<=ny and ny<n:
            if ny==n-1 and dir==2:
                continue
            if cost+mars[ny][nx]<dp[1][ny][nx]:
                continue
            if cost+mars[ny][nx]>dp[dir][ny][nx]:
                #walks[w+1]=cost+mars[ny][nx]
                #chk[2-dir][y][x]=True
                dp[dir][ny][nx]= cost+mars[ny][nx]
                q.append((-dp[dir][ny][nx],ny, nx,dir,w+1))

print(ans)