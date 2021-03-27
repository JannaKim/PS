import sys; input= lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(100000)

#rotate

def rotate(r, c, puz):
    new= [[0]*r for _ in range(c)]
    #[print(*el) for el in new]
    #print()
    #[print(*el) for el in puz]
    #print()
    for i in range(r):
        for j in range(c):
            new[j][r-1-i] = puz[i][j]
    return new


n1, m1= map(int, input().split())
one=[]
for _ in range(n1):
    one.append(list(map(int, list(input()))))

n2, m2= map(int, input().split())
two=[]
for _ in range(n2):
    two.append(list(map(int, list(input()))))


def fit(y, x, pan):
    tmp= [el[:] for el in pan]
    ay, ax= 1e9, 1e9
    by, bx= 0, 0

    for sy, i in enumerate(range(y,y+n2)):
        for sx, j in enumerate(range(x,x+m2)):
            tmp[i][j]+= two[sy][sx]
            if tmp[i][j]==2:
                return 1e9
    for i in range(len(pan)):
        for j in range(len(pan[0])):
            if tmp[i][j]:
                ay= min(ay, i)
                ax= min(ax, j)
                by= max(by, i)
                bx= max(bx, j)
    return (by-ay+1)*(bx-ax+1)


mn=1e9
ans=1e9
ths= [el[:] for el in one]
for k in range(4): # 4각도 다
    #[print(*el) for el in ths]
    #print()
    y, x,hei,wid= 0,0,0,0
    if not k%2:
        hei,wid =n1,m1
    else:
        hei,wid= m1, n1
    y=n2
    x=m2
    board=[[0]*(wid+2*m2) for _ in range(hei+2*n2)]
    #[print(*el) for el in board]
    for sy, i in enumerate(range(y,y+hei)):
        for sx, j in enumerate(range(x,x+wid)):
            #print(i, j, sy, sx)
            board[i][j]=ths[sy][sx]

    #[print(*el) for el in board]
    #print()

    for i in range(0,hei+2*n2-n2+1):
        for j in range(0,wid+2*m2-m2+1):
            #print(i, j, fit(i, j, board))
            ans=min(ans, fit(i, j, board))

    ths= rotate(hei,wid,ths)
print(ans)

'''
세로: 세로1+2*(세로2-1)
가로: 가로1+2*(가로2-1)

3 5
11111
10001
11111
1 2
10
'''
