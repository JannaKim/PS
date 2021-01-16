import sys;  input = lambda: sys.stdin.readline().rstrip()
from collections import deque
n = int(input())
r = range
sea=[]
sea.append([-1]*(n+2))
sea += [[-1]+ list(map(int,input().split()))+[-1] for _ in r(n)]
sea.append([-1]*(n+2))
pos = [(y,x) for x in r(1,n+1) for y in r(1,n+1) if sea[y][x] == 9][0]
lv = 2
sea[pos[0]][pos[1]] = 0

Dx = [0,-1,1,0]
Dy = [-1,0,0,1]

v=[[False] for _ in r(n+2) for __ in r(n+2)]

def get_next_pos(sy, sx, lv):

    q = deque()
    q.append((sy, sx, 0))

    #print(sy,sx)
    while q:
        cy, cx, count = q.popleft()
        fish = sea[cy][cx]
        print(f'fish{fish}, {cy}, {cx}')

        # found
        if fish in r(1,lv): 
            cands = [(cy, cx, count)]
            while q and q[0][2] == cands[0][2]:
                cy, cx, count = q.popleft()
                if sea[cy][cx] in r(1,lv):
                    cands.append((cy, cx, count))         
            cands.sort()
            return cands[0]

        if fish not in (0, lv): # unable to step more
            continue
        
        #cur loc: 0 or lv
        for dy,dx in zip(Dy,Dx):
            ny, nx = cy+dy, cx+dx
            if sea[ny][nx]<0 or v[ny][nx]:
                continue
            v[ny][nx]=True
            q.append((ny, nx, count + 1))
            
    return False

ans = 0
next_state = get_next_pos(pos[0], pos[1], lv)
exp = 0
while next_state:
    y,x,cnt = next_state
    # eaten
    sea[y][x] = 0
    #[print(*el) for el in sea]
    #print()
    exp += 1
    if exp == lv:
        lv += 1
        exp = 0
    ans += cnt
    next_state = get_next_pos(y,x,lv)
    print( get_next_pos(y,x,lv))
print(ans)
    
'''
4
4 3 2 1
0 0 0 0
0 0 9 0
1 2 3 4

'''
            while q and q[0][2] == cands[0][2]:
                cur = q.popleft()
                cy, cx, count = cur
                if sea[cy][cx] and sea[cy][cx] < lv:
                    cands.append(cur)         
            cands.sort()
'''
'''