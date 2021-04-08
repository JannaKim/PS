import sys; input= lambda: sys.stdin.readline().rstrip()
r, c= map(int, input().split())
prairie=[list(input()) for _ in range(r)]

Dy= [0,0,1,-1]
Dx= [1,-1,0,0]
for i in range(r):
    for j in range(c):
        if prairie[i][j]=='S':
            for dy, dx in zip(Dy, Dx):
                y= i+dy
                x= j+dx
                if 0<=y and y<r and 0<=x and x<c:
                    if prairie[y][x]=='.':
                        prairie[y][x]='D'
                    elif prairie[y][x]=='W':
                        print(0)
                        exit()
print(1)
for i in range(r):
    print(''.join(prairie[i]))
