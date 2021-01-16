from heapq import*
import sys; input = lambda: sys.stdin.readline().rstrip(); r = range

fish=[0]*17 # 물고기 좌표
fishhead=[0]*17
# fishhead[1]=8-1

sea=[[-1]*6 for _ in r(6)]

for i in r(1,1+4):
    line = [*map(int, input().split())]
    for j in r(1,1+4):
        sea[i][j]= line[2*(j-1)]
        fish[line[2*(j-1)]]= (i,j)
        fishhead[line[2*(j-1)]]= line[2*(j-1)+1]-1


######################################################################################
fish[sea[1][1]]= (0,0)
first=sea[1][1]
sea[1][1]= -2

DY=[-1, -1, 0, 1, 1, 1, 0, -1] # %8
DX=[0, -1, -1, -1, 0, 1, 1, 1]

def moveFish():
    [print(*el) for el in sea]
    print('fish are moving')
    for i in r(1,17):
        cy, cx= fish[i]
        if not cy+cx: continue
        head= fishhead[i]
        
        for j in r(head,head+8):
            ny= cy+DY[j%8]
            nx= cx+DX[j%8]
            # 이동에 성공했다면 회전 상태가 유지됩니다tlqkf
            if sea[ny][nx] in r(1,17):
                fish[i], fish[sea[ny][nx]]= fish[sea[ny][nx]], fish[i]
                sea[cy][cx], sea[ny][nx]= sea[ny][nx], sea[cy][cx]
                fishhead[i]=j%8
                break
            elif not sea[ny][nx]:
                fish[i]= (ny, nx)
                sea[cy][cx], sea[ny][nx]= 0, sea[cy][cx]
                fishhead[i]=j%8
                break
        [print(*el) for el in sea]
mx=0
def dfs(y, x, exp, lastfish):
    global mx
    global sea
    global fish
    global fishhead
    head= fishhead[lastfish]
    print('exp', exp, 'lastfish', lastfish)
    
    moveFish()
    print('fish moved')
    [print(*el) for el in sea]
    print()
    

    ny= y
    nx= x
    canMove= False
    for _ in r(3):
        ny+= DY[head]
        nx+= DX[head]
        if sea[ny][nx]<0: break
        if sea[ny][nx]>0:
            print(f'cy cx {y} {x}-> ny nx {ny} {nx}')
            print(f'before meal')
            [print(*el) for el in sea]
            prv= [[sea[i][j] for j in r(6)] for i in r(6)] # most efficient way?
            prv_fish= [fish[i] for i in r(17)]
            prv_fishhead= [fishhead[i] for i in range(17)]

            canMove= True
            sea[y][x]=0
            eaten= sea[ny][nx]
            sea[ny][nx]=-2
            fish[eaten]=(0,0)
            print('eat')
            [print(*el) for el in sea]
            print()
            dfs(ny, nx, exp+eaten, eaten)
            sea= [[prv[i][j] for j in r(6)] for i in r(6)]
            fish= [prv_fish[i] for i in r(17)]
            fishhead= [prv_fishhead[i] for i in range(17)]
    if not canMove:
        [print(*el) for el in sea]
        print(exp)
        mx= max(mx, exp)


[print(*el) for el in sea]
print()
dfs(1,1,first, first)

print(mx)