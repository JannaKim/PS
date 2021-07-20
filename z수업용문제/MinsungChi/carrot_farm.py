

n, cx, cy = map( int, input().split(' '))
L=[]
for i in range(0, n):
    L.append(['.']*n)
for i in range(0, n):
    for j in range(0, n):
        if (i+j)%2== (cx + cy)%2:
            L[i][j]='v'
for k in range(0,n):
    print(*L[k], sep= '')

