# 77% RTE
import sys; input= lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(300000)
n, m= map(int, input().split())
mp=[[*map(int,list(input()))] for _ in range(n)] 
ans=[el[:] for el in mp]
#[print(*el) for el in mp]
chk= [[0]*m for _ in range(n)]
Dy= [0,0,1,-1]
Dx= [1,-1,0,0]

def dfs(y,x):
    tmp=1
    for dy, dx in zip(Dy, Dx):
        ny= y+dy
        nx= x+dx
        if 0<=ny<n and 0<=nx<m:
            if not mp[ny][nx] and not chk[ny][nx]:
                chk[ny][nx]=1
                
                tmp+=dfs(ny,nx)
    return tmp # %10 하면 안되는 이유?
same=[[-1]*m for _ in range(n)]
def fill(y, x, c,a):
    for dy, dx in zip(Dy, Dx):
        ny= y+dy
        nx= x+dx
        if 0<=ny<n and 0<=nx<m:
            if not mp[ny][nx] and chk[ny][nx]==1:
                chk[ny][nx]=2
                mp[ny][nx]=c
                same[ny][nx]=a
                fill(ny,nx,c,a)

a=0
for i in range(n):
    for j in range(m):
        if not mp[i][j]:
            chk[i][j]=1
            cnt=dfs(i,j)
            mp[i][j]=-cnt
            same[i][j]=a
            fill(i,j,-cnt,a)
            a+=1


for i in range(n):
    for j in range(m):
        if mp[i][j]==1:
            tmp=0
            ch=dict()
            for dy, dx in zip(Dy, Dx):
                ny= i+dy
                nx= j+dx
                
                if 0<=ny<n and 0<=nx<m:
                    if mp[ny][nx]<0:
                        if same[ny][nx] not in ch:
                            ch[same[ny][nx]]=1
                            tmp-=mp[ny][nx]
                            tmp%=10
            ans[i][j]=(tmp+1)%10

[print(''.join(list(map(str,el)))) for el in ans]