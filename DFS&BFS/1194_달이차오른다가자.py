import sys; input= lambda: sys.stdin.readline().rstrip()
from collections import deque
#2500*50 ok
n, m= map(int, input().split())
maze=[list(input()) for _ in range(n)]

st=[0,0]
for i in range(n):
    for j in range(m):
        if maze[i][j]=='0':
            st=[i,j]
            break

Dy= [0,1,-1,0]
Dx= [1,-0,0,-1]
chk=[[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        chk[i][j]={}
q=deque()
q.append((st[0], st[1], 0,0))
while q: 
    y, x, w,keys= q.popleft()
    #print(y,x,w,bin(keys))
    ret= []
    for dir,(dy, dx) in enumerate(zip(Dy, Dx)):
        ny=y+dy
        nx=x+dx
        if ny<0 or n<=ny or nx<0 or m<=nx:
            continue
        #print(ny,nx)
        if keys in chk[ny][nx]:# 얘입장에서 가본곳이다
            continue
        #print(ny,nx)
        if maze[ny][nx]=='#': continue
        if maze[ny][nx]=='.' or maze[ny][nx]=='0' :
            chk[ny][nx][keys]=True
            q.append((ny,nx,w+1,keys))
            
        elif maze[ny][nx]=='1':
            print(w+1)
            exit()
        else:
            ths=ord(maze[ny][nx])
            if ths<=96: # door
                ths-=65
                #print('door spot')
                if keys|(1<<ths)==keys: # 열쇠있다 keys&(1<<ths)
                    #print('o')
                    chk[ny][nx][keys|(1<<ths)]=True
                    q.append((ny, nx, w+1,keys))
                    
            else: # key
                ths-=97
                #print('key spot')
                chk[ny][nx][keys|(1<<ths)]=True
                q.append((ny, nx, w+1,keys|(1<<ths)))
                        
print(-1)

'''
1F....f
A.....a
#....##
....0..
11
4 7
1F....f
A.....a
#....##
....Aa0

2 7
1F.f#.0
A...#.a

2 7
1F.f..0
A.....a

4 7
1F....f
A.....a
#....##
....0..


4 7
1F....f
A.....a
###.###
....Ff0

4 7
1FD...f
AC....a
#.....#
cd....0



8 14
1FD...b#....f#
AC.....#.....#
#.....##.....#
#cd....AC....a
1BD....#.....#
AC.....AC.....
#.....#.......
.............0

4 5
#f#..
#.#..
#a#..
0.FA1
10
'''

