from heapq import*
import sys; input = lambda: sys.stdin.readline().rstrip();
r, c, d = map(int, input().split())
field= [[-1]*(c+2)]
field+=[[-1]+[*map(int, input().split())]+[-1] for _ in range(r)]
field+=[[-1]*(c+2)]
# archer
Dy= [0, -1, 0]
Dx= [-1, 0, 1]
chosen=[]

def bfs(floor, kill):
    print('chosen:',chosen)
    print(floor, kill)
    loc= set()
    for i in range(3):
        #[print(*el) for el in field]
        print(f'field[{floor-1}][{chosen[i]}]: {field[floor-1][chosen[i]]}')
        if field[floor-1][chosen[i]]==1:
            loc.add((floor-1,chosen[i]))
            continue

        v=[[False]*(c+2) for _ in range(r+2)]
        v[floor-1][chosen[i]]=True
        q = [(1,chosen[i], floor-1)]

        while q:
            steps, cx, cy = heappop(q)
            if steps>=d: break
            isFoe= field[cy][cx]
            if isFoe:
                loc.add((cy,cx))
            for dy,dx in zip(Dy,Dx):
                ny, nx = cy+dy, cx+dx
                if field[ny][nx]==1: # foe found
                    loc.add((ny,nx))
                    q=[]
                    break
                elif not field[ny][nx]:
                    v[ny][nx]=True
                    heappush(q,(steps + 1, nx, ny))
    if floor==1: return kill
    for y, x in loc:
        field[y][x]=0
    return bfs(floor-1,kill+len(loc))

mx=0
def backtrack(i, num):
    global mx
    global d
    global field
    if num==3:
        #print(chosen)
        prv= [[field[i][j] for j in range(c+2)] for i in range(r+2)]
        mx = max(mx, bfs(r+1, 0))
        field= [[prv[i][j] for j in range(c+2)] for i in range(r+2)]
        return
    if c-i+num<3: return
    if i==c:return
    chosen.append(i+1)
    backtrack(i+1,num+1)
    chosen.pop()
    backtrack(i+1,num)

backtrack(0,0)
print(mx)