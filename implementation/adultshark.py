from sys import *; input = lambda: stdin.readline().rstrip(); r = range
n, m, k = map(int, input().split())
sea=[[-2]*(n+2)]
sea += [[-2]+ [int(i)-1 for i in input().split()]+ [-2] for _ in r(n)]
sea +=[[-2]*(n+2)]
head = [int(i)-1 for i in input().split()]
flock = {} 
for i in r(1,1+n):
    for j in r(1,1+n):
        if sea[i][j]>=0:
            flock[sea[i][j]] = [i, j, head[sea[i][j]]] 
        sea[i][j] = None
priorities=[]
priorities+=[[int(i)-1 for i in input().split()] for _ in r(m * 4)]

########################################################################################

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

#[print(*el) for el in sea]
#print()
time = -1
while time <= 1000:
    if len(flock) == 1:
        print(time)
        exit(0)

    alive = list(flock.keys())
    alive.sort()  
    for shark in alive:
        #print(index,'\n')
        if sea[flock[shark][0]][flock[shark][1]] is None:  # movable
            sea[flock[shark][0]][flock[shark][1]] = [shark, k]  
        elif sea[flock[shark][0]][flock[shark][1]][0] == shark:  # own property
            sea[flock[shark][0]][flock[shark][1]] = [shark, k]
        else:  # defeated
            del flock[shark]
        #[print(*el) for el in sea]
        #print()

    # move sharks
    alive = list(flock.keys())
    alive.sort()
    for shark in alive:
        cy, cx, cd = flock[shark] 

        new_place = False
        for i in priorities[shark * 4 + cd]: # try: based on priorities
            ny, nx, nd = cy + dy[i], cx + dx[i], i
            if sea[ny][nx]!=-2:
                if sea[ny][nx] is None:  # if movable
                    new_place = True 
                    flock[shark] = [ny, nx, nd]
                    break

        if not new_place: 
            for i in priorities[shark * 4 + cd]:
                ny, nx, nd = cy + dy[i], cx + dx[i], i
                if sea[ny][nx]!=-2:
                    if sea[ny][nx][0] == shark:  # its own property
                        flock[shark] = [ny, nx, nd]
                        break
        else:
            continue


    # 1 sec past
    for i in r(1,1+n): 
        for j in r(1,1+n):
            if sea[i][j] is not None:
                sea[i][j][1] -= 1 # smell -1
                if sea[i][j][1] == 0:  # smell 0: delete property
                    sea[i][j] = None

    time += 1

print(-1)

'''
        if not old_space:  # impossi
            del flock[shark]  # cur shark died
'''
'''
import sys
read = sys.stdin.readline
n, m, k = map(int, read().split())
arr = [[[1001, 1001] for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j, v in enumerate(map(int, read().split())):
        if v < 1: continue
        arr[i][j] = [-v, k]
d = [*map(int, read().split())]
l = [[[*map(int, read().split())] for _ in range(4)] for _ in range(m)]
cnt = m
dd = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for ans in range(1, 1001):
    tmp = [[[1001, 1001] for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if arr[i][j][0] > 0: continue
            a = -arr[i][j][0]
            flag = True
            for b in l[a-1][d[a-1]-1]:
                dx, dy = dd[b-1]
                if -1 < i+dx < n and -1 < j+dy < n:
                    if arr[i+dx][j+dy][0] == 1001:
                        d[a-1] = b
                        break
                    elif flag and arr[i+dx][j+dy][0] == a:
                        flag = False
                        d[a-1] = b
            dx, dy = dd[d[a-1]-1]
            if tmp[i+dx][j+dy][0] == 1001:
                tmp[i+dx][j+dy] = [-a, k]
                arr[i][j] = [a, k]
            else:
                if -tmp[i+dx][j+dy][0] > a:
                    tmp[i+dx][j+dy] = [-a, k]
                arr[i][j] = [a, k]
                cnt -= 1
    for i in range(n):
        for j in range(n):
            if tmp[i][j][0] < 0 \
                    or arr[i][j][0] == 1001 \
                    or arr[i][j][1] == 1: continue
            tmp[i][j] = [arr[i][j][0], arr[i][j][1] - 1]
    if cnt == 1: print(ans);exit()
    arr = tmp
print(-1)
'''


'''
from sys import*
from collections import*
input=stdin.readline
def move(x, y, s, d, f, dic):
    for j in range(4):
        nd = pd[s-1][d][j]
        dx, dy = dd[nd]
        nx, ny = x+dx, y+dy
        if nx<0 or ny<0 or nx>n-1 or ny>n-1: continue
        if f==0 and visit[nx][ny]: continue
        if f==1 and visit[nx][ny][1] == s:
            dic[nx, ny] = [s, nd]
            return 1
        if f==0:
            if (nx, ny) not in dic:
                dic[nx, ny] = [s, nd]
            else:
                if dic[nx, ny][0] > s:
                    dic[nx, ny] = [s, nd]
            return 1
    return 0
def solve():
    global visit
    q=deque()
    visit = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if a[i][j]:
                visit[i][j] = [k-1, a[i][j]]
                q.append((i, j, a[i][j], defaultD[a[i][j]-1]-1))
    for t in range(1001):
        lq = len(q)
        if lq == 1: return t
        dic = {}
        for i in range(lq):
            x, y, s, d = q.popleft()
            if not move(x, y, s, d, 0, dic):
                move(x, y, s, d, 1, dic)
        for i in range(n):
            for j in range(n):
                if visit[i][j] and visit[i][j][0] <= t:
                    visit[i][j]=0
        for (x, y), (s, d) in dic.items():
            visit[x][y] = [k+t, s]
            q.append((x, y, s, d))
    return -1
dd=[(-1,0),(1,0),(0,-1),(0,1)]
n, m, k = map(int,input().split())
pd = [[]for _ in range(m)]
a=[list(map(int,input().split()))for _ in range(n)]
defaultD = list(map(int,input().split()))
for i in range(m):
    for j in range(4):
        temp=list(map(int,input().split()))
        pd[i].append([x-1 for x in temp])
print(solve())
'''


'''
import sys
read = sys.stdin.readline
n, m, k = map(int, read().split())
arr = [[[1001, 1001] for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j, v in enumerate(map(int, read().split())):
        if v < 1: continue
        arr[i][j] = [-v, k]
d = [*map(int, read().split())]
l = [[[*map(int, read().split())] for _ in range(4)] for _ in range(m)]
cnt = m
dd = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for ans in range(1, 1001):
    tmp = [[[1001, 1001] for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if arr[i][j][0] > 0: continue
            a = -arr[i][j][0]
            flag = True
            for b in l[a-1][d[a-1]-1]:
                dx, dy = dd[b-1]
                if -1 < i+dx < n and -1 < j+dy < n:
                    if arr[i+dx][j+dy][0] == 1001:
                        d[a-1] = b
                        break
                    elif flag and arr[i+dx][j+dy][0] == a:
                        flag = False
                        d[a-1] = b
            dx, dy = dd[d[a-1]-1]
            if tmp[i+dx][j+dy][0] == 1001:
                tmp[i+dx][j+dy] = [-a, k]
                arr[i][j] = [a, k]
            else:
                if -tmp[i+dx][j+dy][0] > a:
                    tmp[i+dx][j+dy] = [-a, k]
                arr[i][j] = [a, k]
                cnt -= 1
    for i in range(n):
        for j in range(n):
            if tmp[i][j][0] < 0 \
                    or arr[i][j][0] == 1001 \
                    or arr[i][j][1] == 1: continue
            tmp[i][j] = [arr[i][j][0], arr[i][j][1] - 1]
    if cnt == 1: print(ans);exit()
    arr = tmp
print(-1)
'''


'''
from sys import*
from collections import*
input=stdin.readline
def move(x, y, s, d, f, dic):
    for j in range(4):
        nd = pd[s-1][d][j]
        dx, dy = dd[nd]
        nx, ny = x+dx, y+dy
        if nx<0 or ny<0 or nx>n-1 or ny>n-1: continue
        if f==0 and visit[nx][ny]: continue
        if f==1 and visit[nx][ny][1] == s:
            dic[nx, ny] = [s, nd]
            return 1
        if f==0:
            if (nx, ny) not in dic:
                dic[nx, ny] = [s, nd]
            else:
                if dic[nx, ny][0] > s:
                    dic[nx, ny] = [s, nd]
            return 1
    return 0
def solve():
    global visit
    q=deque()
    visit = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if a[i][j]:
                visit[i][j] = [k-1, a[i][j]]
                q.append((i, j, a[i][j], defaultD[a[i][j]-1]-1))
    for t in range(1001):
        lq = len(q)
        if lq == 1: return t
        dic = {}
        for i in range(lq):
            x, y, s, d = q.popleft()
            if not move(x, y, s, d, 0, dic):
                move(x, y, s, d, 1, dic)
        for i in range(n):
            for j in range(n):
                if visit[i][j] and visit[i][j][0] <= t:
                    visit[i][j]=0
        for (x, y), (s, d) in dic.items():
            visit[x][y] = [k+t, s]
            q.append((x, y, s, d))
    return -1
dd=[(-1,0),(1,0),(0,-1),(0,1)]
n, m, k = map(int,input().split())
pd = [[]for _ in range(m)]
a=[list(map(int,input().split()))for _ in range(n)]
defaultD = list(map(int,input().split()))
for i in range(m):
    for j in range(4):
        temp=list(map(int,input().split()))
        pd[i].append([x-1 for x in temp])
print(solve())
'''