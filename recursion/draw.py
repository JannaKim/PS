inp = int(input())
n = inp ** 3

mp = [[' ']*(n+15) for _ in range(n)]
base = n+4
bound = 3*2
mp[-5][base:base + 5] =[1,' ',2,' ',3] 
def rec(y , x , k):
    global n
    if k==1:
        #mp[y][x] = '*'
        return
    for i in range(n):
        for j in range(n):
            if abs(y - i) + abs(x - j) == k:
                mp[i][j] = '*'
    
    nxt = k//2
    for ny , nx in ( (y-nxt , x - nxt) , (y - nxt , x + nxt) , (y + nxt , x - nxt) , (y + nxt , x + nxt)):
        rec(ny , nx , nxt)
    


rec(n//2 , n//2 , n//2)

mp[0][0] = '#'

Dy = [0,1,0,-1]
Dx = [1,0,-1,0]
dir = {'d':0 , 's':1 , 'a':2 , 'w':3}
#[print(*el) for el in mp]
power = [1 , 2 , 3]
state = [True , True , True]

def chk(y , x , d):
    ny , nx = y , x
    cnt = 0
    while mp[ny ][nx] =='*':
        print(ny,  nx)
        cnt += 1
        ny , nx = ny + Dy[ d ] , nx + Dx[ d ]
    return cnt
y , x = 0 , 0

# def movable(y , x , dir):
#     if H[y][x]
H = [ [ [False] * 4 for _ in range(n)] for __ in range(n)]
recent = -1
while True:
    print(state)
    for i in range(0,bound,2):
        mp[-4][i+base] = power[i//2]
        mp[-4][i+base] = 'o' if state[i//2] == True else 'x'

    [print(*el) for el in mp]
    mv = input()
    mv = dir[mv]
    ny , nx = y + Dy[mv] , x + Dx[mv]
    nxt = chk(ny , nx , mv)
    print(nxt , y , x ,' ', ny , nx)
    if nxt:
        if not state[nxt-1] or nxt>3:
            continue
        else:
            recent = nxt
            sy, sx = ny + nxt * Dy[mv] , nx + nxt * Dx[mv]
            print('s' , sy , sx)
            mp[sy][sx] = '*'
            state[nxt-1] = False
            #print(state)
    else:
        mp[y][x] , mp[ny][nx] = ' ', '#'           
        y , x = ny , nx

    for i in range(1,1+3):
        if i != recent and not state[i-1]:
            state[i-1] = True
            break
    #print(y , x , ny , nx)
    mp[y][x] , mp[ny][nx] = ' ', '#'
    y , x = ny , nx
    print(mp[y][x])



    # mp[-1][base:6] =[True if el == 'o' else 'x' for el in state]

    # for i in range(n+5 , n+5+3):
    #     if mp[-1][base + i]
    #break