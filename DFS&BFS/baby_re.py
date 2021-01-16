from heapq import*
import sys; input = lambda: sys.stdin.readline().rstrip(); r = range
n = int(input())
sea=[]
sea.append([-1]*(n+2))
sea += [[-1]+ [*map(int,input().split())]+[-1] for _ in r(n)]
sea.append([-1]*(n+2))

######################################################################################

pos_shark = [(y,x) for x in r(1,n+1) for y in r(1,n+1) if sea[y][x] == 9][0]
lv = 2
sea[pos_shark[0]][pos_shark[1]] = 0

Dx = [0,-1,1,0]
Dy = [-1,0,0,1]

def next_food(sy, sx): # found loc, total steps
    global lv
    q=[(0, sy, sx)]
    v=[[False for _ in r(n+2)] for __ in r(n+2)]

    while q:
        cnt, cy, cx = heappop(q)
        hp_fish = sea[cy][cx]

        # found
        if hp_fish in r(1,lv):
            return (cy, cx, cnt)

        if hp_fish not in (0, lv):
            continue
        
        for dy,dx in zip(Dy,Dx):
            ny, nx = cy+dy, cx+dx
            if sea[ny][nx]<0 or v[ny][nx]:
                continue
            v[ny][nx]= True
            heappush(q,(cnt + 1, ny, nx))
            
    return False

ans = 0
exp = 0
valid = next_food(pos_shark[0], pos_shark[1])
while valid:
    y,x,steps = valid
    # eaten
    sea[y][x] = 0
    exp += 1
    if exp == lv: 
        lv += 1
        exp = 0
    ans += steps
    valid = next_food(y,x)

print(ans)
    
