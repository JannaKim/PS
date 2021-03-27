from collections import deque
n, m= map(int, input().split())
lab= [[-1]*(n+2)]
lab+= [[-1]+[*map(int, input().split())]+[-1] for _ in range(n)]
lab+=[[-1]*(n+2)]

# count possi loc
loc=0
v=[]
for i in range(1,n+1):
    for j in range(1,n+1):
        if lab[i][j]==2:
            loc+=1
            v.append((i,j))
        if lab[i][j]==1:
            lab[i][j]=-1

chk= [False]*loc

dy= [0,0,1,-1]
dx= [1,-1,0,0]

def isFilled(L):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if L[i][j] in (0,2):
                return False
    return True

def spread():
    experi=[]
    for el in lab:
        experi.append(el[:])
    #[print(*el) for el in experi]
    q=deque()
    for i in range(loc):
        if chk[i]:
            q.append((v[i],0))
            l, m= v[i]
            experi[l][m]=1
    time=0
    if isFilled(experi): # filled right at this moment!
        return time
    #print(q)
    while q:
        (a,b),t= q.popleft()
        for y, x in zip(dy,dx):
            if time<t: # 시간바꼈으면 바이러스별로 그 시간대를 다 돌린것
                #print('time=',t)
                time+=1
                #[print(*el) for el in experi]
                #print()
                if isFilled(experi):
                    return time
            if experi[a+y][b+x]!=1 and experi[a+y][b+x]>=0: # 바이러스 뿌려지지않았고 벽이 아니면
                experi[a+y][b+x]=1
                q.append(((a+y, b+x), t+1))
    return 1e9

def backtrack(i,cnt):
    if cnt==m:
        #print(chk)
        return spread()
    if i==loc:
        return 1e9
    tmp=1e9
    chk[i]=True
    tmp= min(tmp, backtrack(i+1,cnt+1))
    chk[i]=False
    tmp= min(tmp, backtrack(i+1,cnt))
    return tmp

ans=backtrack(0,0)
if ans==1e9:
    print(-1)
else:
    print(ans)

