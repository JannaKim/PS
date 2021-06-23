'''
ny nx chk and nynx * y x == 42: found
chk 물 1 백조1 6 백조2 7
'''
#from time import sleep
from collections import deque
import sys; input = lambda: sys.stdin.readline().rstrip()
r , c = map(int, input().split())
river = [ input() for _ in range(r)]

Dy = [0,0,1,-1]
Dx = [1,-1,0,0]
chk = [ [0]*c for _ in range(r)]
# find swan
kk = 0

q = deque()

def bound(y , x):
    if 0<=y<r and 0<=x<c:
        return True
    return False

def swim(y , x):
    dq = deque()
    dq.append( (y , x))
    while dq:
        y , x = dq.popleft()
        for dy , dx in zip(Dy, Dx):
            ny , nx = y + dy , x + dx
            if bound(ny , nx) and chk[ny][nx]>0 and chk[ny][nx]!=chk[y][x]:
                if chk[y][x]*chk[ny][nx] == 42:
                    return True
                else:
                    chk[ny][nx] = chk[y][x]
                    dq.append( (ny , nx))
    return False

'''
6 7 7
day * 4* q1  + day * 4 *q2 + ...
'''

def rivermeets(y , x , ny , nx):
    if chk[y][x]*chk[ny][nx] == 42:
        return True
    elif chk[y][x]==1 and chk[ny][nx]>1:
        if swim(ny , nx):
            return True
    elif chk[y][x]>1 and chk[ny][nx]==1:
        if swim(y , x):
            return True
    return False

def bfs(newq , q ,  switch):
    #print(q)
    res = False
    for y , x in q:
        for dy,  dx in zip(Dy , Dx):
            ny = y + dy
            nx = x + dx
            if bound(ny , nx):
                if not chk[ny][nx]:
                    chk[ny][nx] = chk[y][x]
                    newq.append(( ny , nx) )

                res |=  rivermeets(y , x , ny , nx)

    return (newq , res)


flag= False
swan = []
for i in range(r):
    for j in range(c):
        if not chk[i][j] and river[i][j] == '.':
            chk[i][j] = 1
            q.append((i , j))
        elif not chk[i][j] and river[i][j] == 'L':
            if flag:
                chk[i][j] = 7
            elif not flag:
                chk[i][j] = 6
                flag=True
            q.append((i , j))
            swan.append( (i , j))

for y , x in swan:
    swim(y , x)


def melt(q):  
    day = 1
    while True:
        newq = deque()
        #sleep(1)
        # print(day)
        # print()
        # for row in range(r):
        #     for col in range(c):
        #         if chk[row][col]== 6:
        #             print('+',end=' ')
        #         elif chk[row][col] == 7:
        #             print('*',end=' ')
        #         elif chk[row][col]:
        #             print('.',end=' ')
        #         else:
        #             print('X',end=' ')
        #     print()
        # #print(*chk , sep = '\n' , end = '\n'*2)
        
        newq , found = bfs(newq , q, 0)
        if found:
            return day
        q = deque()
        for el in newq:
            y , x = el
            for dy,  dx in zip(Dy , Dx):
                ny = y + dy
                nx = x + dx
                if bound(ny , nx) and chk[ny][nx]:
                    if rivermeets(y , x , ny , nx):
                        return day
            q.append(el)
        day += 1


print(melt(q))
for row in range(r):
    for col in range(c):
        if chk[row][col]== 6:
            print('.',end='')
        elif chk[row][col] == 7:
            print('*',end='')
        elif chk[row][col]:
            print(' ',end='')
        else:
            print('█',end='')
    print()
#print(*chk , sep = '\n')

#print(kk)


'''
8 17
LXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXL

1 5
LXXXL

1 4
LXXL

.XX.
'''

