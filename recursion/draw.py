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
        cnt += 1
        ny , nx = ny + Dy[ d ] , x + Dx[ d ]
    return cnt
y , x = 0 , 0
while True:
    print(state)
    for i in range(0,bound,2):
        mp[-4][i+base] = power[i//2]
        mp[-4][i+base] = 'o' if state[i//2] == True else 'x'

    [print(*el) for el in mp]
    mv = input()
    ny , nx = y + Dy[ dir[mv] ] , x + Dx[ dir[mv]]
    nxt = chk(ny , nx , dir[mv])
    print(nxt)
    if nxt:
        if not state[nxt-1] or nxt>=3:
            continue
        else:
            crossdir = (dir[mv]+2)%4
            crossdir = dir[mv]
            print(ny , nx)
            for i in range(nxt+1 , 0 , -1):
                mp[y + i * Dy[crossdir]][x + i * Dx[crossdir]] = mp[y + (i-1) * Dy[crossdir]][x + (i-1) * Dx[crossdir]] 
                mp[y + (i-1) * Dy[crossdir]][x + (i-1) * Dx[crossdir]]  = ' '
            
            state[nxt-1] = False
            print(state)
    else:
        mp[y][x] , mp[ny][nx] = ' ', '#'
        y , x = ny , nx

    for i in range(1,1+3):
        if i != nxt and not state[i-1]:
            state[i-1] = True
            break
    print(y , x , ny , nx)
    mp[y][x] , mp[ny][nx] = ' ', '#'
    y , x = ny , nx
    print(mp[y][x])



    # mp[-1][base:6] =[True if el == 'o' else 'x' for el in state]

    # for i in range(n+5 , n+5+3):
    #     if mp[-1][base + i]
    #break