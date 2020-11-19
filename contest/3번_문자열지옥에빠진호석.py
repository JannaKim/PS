import sys
sys.setrecursionlimit(int(1e9))
dx = [0,0,1,-1, 1,1,-1,-1]
dy = [1,-1,0,0, -1,1,-1,1]
N, M, K = map(int, input().split())

mp=[]
for _ in range(N):
    mp.append(input())
#[print(i) for i in mp]
#0 1 2 3 %4
#y%N, x%M
S=0

def f(i,j,g,idx,last):
    global S
    for y, x in zip(dy,dx):
        if i+y<0 and j+x>=0:
            if mp[M+i+y][(j+x)%M]==g[idx]:
                if idx==last:
                    S+=1
                else:
                    f(M+i+y,(j+x)%M,g,idx+1,last)
        elif i+y>=0 and j+x<0:
            if mp[(i+y)%N][M+j+x]==g[idx]:
                if idx==last:
                    S+=1
                else:
                    f((i+y)%N,M+j+x,g,idx+1,last)
        elif i+y<0 and j+x<0:
            if mp[M+i+y][M+j+x]==g[idx]:
                if idx==last:
                    S+=1
                else:
                    f(M+i+y,M+j+x,g,idx+1,last)
        else:
            if mp[(i+y)%N][(j+x)%M]==g[idx]:
                if idx==last:
                    S+=1
                else:
                    f((i+y)%N,(j+x)%M,g,idx+1,last)
    

for _ in range(K):
    S = 0
    g = input()
    for i in range(N):
        for j in range(M):
            if mp[i][j]==g[0]:
                f(i,j,g,1,len(g)-1)#좌표, 문자, 몇번째
            #print(f'{i},{j} 시작까지 총 {S}개')
    print(S)

