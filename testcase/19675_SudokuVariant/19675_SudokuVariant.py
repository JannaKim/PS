import sys; input= lambda: sys.stdin.readline().rstrip()
import time
mp= [[*map(int, input().split())] for _ in range(3)]
ans=0
def backtrack(t):
    global z
    if z==t:
        global ans
        ans+=1
        return
    print(t)
    [print(*el) for el in mp]
    
    time.sleep(0.5)
    i, j= ls[t]
    chk=[False]*10
    for r in range(3):
        chk[mp[r][j]]=True
    for c in range(3):
        chk[mp[i][c]]=True
    #print(chk)
    for k in range(1,10):
        if not chk[k]:
            chk[k]=True
            mp[i][j]=k
            backtrack(t+1)
            
            mp[i][j]=0
z=0
ls=[]
for i in range(3):
    for j in range(3):
        if not mp[i][j]:
            z+=1
            ls.append((i, j))
if not z:
    print(0)
    exit()

backtrack(0)
print(ans)