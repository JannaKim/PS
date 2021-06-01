# 2500s,* (50+50)
import sys; input= lambda: sys.stdin.readline().rstrip()
from collections import deque
r, c= map(int, input().split())
forest= [input() for _ in range(r)]

water=[]
chk=[[0]*c for _ in range(r)]
for i in range(r):
    for j in range(c):
        if forest[i][j]=='*':
            water.append((i,j))
            chk[i][j]= 1
        if forest[i][j]=='S':
            st= (i,j)
        if forest[i][j]=='D':
            ed= (i,j)
Dy= [0,0,1,-1]
Dx= [1,-1,0,0]
dp= [[1e9]*c for _ in range(r)]
q= deque()
q.append((st[0],st[1],1))
dp[st[0]][st[1]]=0
wat=0
while q:
    y, x, dur= q.popleft()
    if (y,x)==ed:
            print(dur-1)
            #[print(*el) for el in dp]
            exit() ##
    if wat<dur: # '다음시간'에 물이 찰 예정인..
        wat=dur
        tmp= water[:]
        water=[]
        for i, j in tmp: # y, x 를 i,j로 받으려니 심적으로 불편하네요.. 왕규님은 이때 인덱스 뭘로 만드세요?
            for dy, dx in zip(Dy, Dx):
                ny= i+dy
                nx= j+dx
                if 0<=ny<r and 0<=nx<c and not chk[ny][nx]:
                    if forest[ny][nx]=='X' or forest[ny][nx]=='D':
                        continue
                    chk[ny][nx]= 1
                    water.append((ny,nx))

    for dy, dx in zip(Dy, Dx):
        ny= y+dy
        nx= x+dx
        if 0<=ny<r and 0<=nx<c:
            if not chk[ny][nx] and forest[ny][nx]!='X':
                if dur<dp[ny][nx]:
                    dp[ny][nx]=dur
                    q.append((ny,nx,dur+1))

print('KAKTUS')
# 띄어쓰기는 다음부터

        