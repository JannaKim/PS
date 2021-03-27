from collections import deque
n= int(input())

board= [[False]*n for _ in range(n)]


y, x, a, b= map(int, input().split())

dir= [(-2,-1), (-2,1), (0,-2), (0,2), (2,-1), (2,1)]

q=[]
q=deque()
q.append((y,x,0))

while q:
    y, x, mv= q.popleft()
    #print(y, x, mv)
    if (y,x)== (a,b):
        print(mv)
        exit()

    for dy, dx in dir:
        #print(y+dy, x+dx)
        if y+dy>=n or x+dx>=n or y+dy<0 or x+dx<0:
            continue
        if not board[y+dy][x+dx]:
            board[y+dy][x+dx]=True
            q.append((y+dy, x+dx,mv+1))

print(-1)