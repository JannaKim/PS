n = int(input())
mp=[['*']*n for _ in range(n)]




def space(ay, ax, by, bx):
    #print(f'space {ay}, {ax}, {by}, {bx}')
    for i in range(ay, by+1):
        for j in range(ax, bx+1):
            mp[i][j]=' '
    



def draw(yi, xi, yj, xj):
    #print(f'draw {yi}, {xi}, {yj}, {xj}')

    gap = (xj-xi+1)//3

    a = (yi+gap, xi+gap)
    b = (yi+gap, xj-gap)
    c = (yj-gap, xi+gap)
    d = (yj-gap, xj-gap)


    space(a[0], a[1], d[0], d[1])
    if a[0]==d[0] and a[1]==d[1] and mp[a[0]][a[1]]==' ': return

    draw(yi,xi,a[0]-1, a[1]-1)
    draw(yi,a[1], b[0]-1, b[1])
    draw(yi, b[1]+1, b[0]-1, xj)

    draw(a[0], xi, c[0], c[1]-1)
    draw(b[0], b[1]+1, d[0], xj)

    draw(c[0]+1, xi, yj, c[1]-1)
    draw(c[0]+1, c[1], yj, d[1])
    draw(d[0]+1, d[1]+1, yj, xj)



draw(0,0,n-1,n-1)

[print(''.join(i)) for i in mp]