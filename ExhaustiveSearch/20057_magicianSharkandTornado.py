import sys; input= lambda: sys.stdin.readline().rstrip()

n= int(input())

sandpit= []
sandpit+= [[*map(int, input().split())] for _ in range(n)]


def rotate(A):
    new= [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            new[j][n-i-1]=A[i][j]
    return new

todo= [i//2 for i in range(2*n, 1, -1)]
todo[0]=n-1

Dy= [-2, -1, -1, 0, 0, 0, 0, 1, 1]
Dx= [0, -1, 1, -1, 1, -2, 2, -1, 1]
percent=[0.05, 0.1, 0.1, 0.07, 0.07, 0.02, 0.02, 0.01, 0.01]
ans=0
def swirl(y, x):
    global ans
    sand= sandpit[y][x]
    sandpit[y][x]=0
    ori=sand

    for dy, dx, p in zip(Dy, Dx, percent):
        ny= y+dy
        nx= x+dx
        s= int(sand*p)
        ori-=s ################################ 내림해서 없어졌으면 ori가 가져감
        if nx<0 or nx>=n or ny<0 or ny>=n:   
            ans+=s
        else:
            sandpit[ny][nx]+=s
    if x<0 or x>=n or y-1<0 or y-1>=n:
        ans+=ori ############################### +=로 안해줌
    else:
        sandpit[y-1][x]+=ori

y=n//2
x=n//2
power=0
while True: #def move(y, x, power):
    #print(y, x, power)
    if not power:
        if not todo:
            break
        sandpit= [el[::1] for el in rotate(sandpit)]
        ny= x
        nx= n-y-1
        power= todo.pop()
        y, x, power= ny, nx, power
    else:
        swirl(y-1,x)
        ny= y-1
        nx= x
        y, x, power= ny, nx, power-1

print(ans)