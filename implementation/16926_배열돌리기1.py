# right , down , left , up
import sys; input= lambda: sys.stdin.readline().rstrip()
dy = [0 , 1 , 0 , -1]
dx = [1 , 0 , -1 , 0]

n , m , rot = map(int, input().split())
mp = [ [*map(int , input().split())] for _ in range(n) ]
def inbound(y , x , floor):
    global n , m
    if 0 + floor <= y < n - floor and 0 + floor <= x < m - floor:
        return True
    return False

def rec(y , x , r , c , floor):
    #print (y , x)
    if r <= 1 or c <= 1:
        return
    global rot
    ls = []
    ls.append( (y , x) )
    
    d = 0
    ny , nx = y , x
    start = True
    while start or (ny != y or nx != x):
        #print(ny , nx)
        start = False
        ny , nx = ny + dy[d] , nx + dx[d]
        #print(ny , nx)
        if not inbound(ny , nx , floor):
            ny -= dy[d]
            nx -= dx[d]
            d = (d + 1) % 4
        else:
            ls.append ( (ny , nx))
    ls.pop()
    tape = (2 * r) + (2 * c) - 4
    new = []
    # print(len(ls) , tape)
    for i in range(rot , rot + tape):
        i %= tape
        new.append( mp[ ls[i][0] ][ ls[i][1] ] )
    for idx , (a , b) in enumerate(ls):
        mp[a][b] = new[idx]

    rec(y + 1 , x + 1 , r - 2 , c - 2 , floor + 1)
    


rec(0 , 0 , n , m , 0)

[print(*el) for el in mp]

