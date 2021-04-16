import sys; input= lambda: sys.stdin.readline().rstrip()
mp= [[*map(int, input().split())] for _ in range(3)]
ans=0
def backtrack():
    flag=False
    for i in range(3):
        for j in range(3):
            if not mp[i][j]:
                flag=True
                chk=[False]*10
                for r in range(3):
                    chk[mp[r][j]]=True
                for c in range(3):
                    chk[mp[i][c]]=True
                for k in range(1,10):
                    if not chk[k]:
                        mp[i][j]=k
                        backtrack()
                        #mp[i][j]=0
                mp[i][j]=0 # 여기다가는 둬야함
                break
                
    if not flag:
        [print(*el) for el in mp]
        global ans 
        ans+=1
flag=True
for i in range(3):
    for j in range(3):
        if not mp[i][j]:
            flag=False
if flag:
    print(0)
    exit()

backtrack()
print(ans)