import sys; input= lambda: sys.stdin.readline().rstrip()
from heapq import heappop, heappush
r, c, ti= map(int, input().split())
mp=[input() for _ in range(r)]
Dy= [0,0,1,-1]
Dx= [1,-1,0,0]

def bfs(y,x):
    q=[]
    heappush(q, (0,y,x,set()))
    chk= [[[] for __ in range(c)] for _ in range(r)]
    ans=0
    while q:
        t,y, x, pot= heappop(q)
        if t==ti:
            ans=max(ans,len(pot))
            continue
        for dy, dx in zip(Dy, Dx):
            ny, nx= y+dy, x+dx
            if 0<=ny<r and 0<=nx<c:
                if mp[ny][nx]=='#':
                    continue
                new= set()|pot
                if mp[ny][nx]=='S':
                    new.add((ny,nx))
                flag=False
                for cs in chk[ny][nx]:
                    if pot&cs==pot:
                        flag=True
                        break
                if not flag:
                    chk[ny][nx].append(new)
                    heappush(q, (t+1,ny,nx,new))
    return ans

st=0
for i in range(r):
    for j in range(c):
        if mp[i][j]=='G':
            print(bfs(i,j))
            exit()
