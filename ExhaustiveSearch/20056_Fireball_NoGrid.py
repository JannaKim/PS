import sys; input= lambda: sys.stdin.readline().rstrip()
dy= [-1, -1, 0, 1, 1, 1, 0, -1]
dx= [0, 1, 1, 1, 0, -1, -1, -1]

n, m, K= map(int, input().split())
Fireballs = []
new=[]
for _ in range(m):
    r, c, m, s, d=  map(int, input().split()) # r, c, m, s, d
    Fireballs.append([r-1,c-1,m,s,d])

def move(tmp, new): # 하나만
    global dx, dy
    for i, j, mass, speed, direction in tmp:
        diry= i+dy[direction%8]*speed
        dirx= j+dx[direction%8]*speed
        while diry<0:
            diry+=n
        while dirx<0:
            dirx+=n
        ny= diry%n
        nx= dirx%n
        new.append([ny, nx, mass, speed, direction%8])

def spreadifConverged(movedOnly, Fireballs):
    if not movedOnly:
        return
    movedOnly.sort()
    basket=[]
    ay, ax, am, aspeed, adir= movedOnly[0]
    by, bx, bm, bspeed, bdir= [0 for underbar in range(5)]
    
    basket.append([ay, ax, am, aspeed, adir])

    for a, b in zip(movedOnly, movedOnly[1:]):

        ay, ax, am, aspeed, adir= a
        by, bx, bm, bspeed, bdir= b
        if ay!=by or ax!=bx:
            if len(basket)==1:
                Fireballs.append(basket[0])
            else:
                arrangedMass, arrangedSpeed= [sum(sp[ths] for sp in basket) for ths in range(2, 4)]
                arrangedMass //= 5
                arrangedSpeed //= len(basket)
                isOdd=True
                isEven=True
                chk=1
                for Im,nt,using,these,dr in basket:
                    if not dr%2: # 짝수
                        isOdd= False
                    elif dr%2:
                        isEven= False
                if not isEven and not isOdd:
                    chk= 1
                else:
                    chk= 0

                if arrangedMass>0 and chk==1: # 홀짝 같이있: x자 이동 1, 3, 5, 7
                    for k in range(1,8,2):
                        Fireballs.append([ay, ax, arrangedMass, arrangedSpeed, k])

                elif arrangedMass>0: # 짝만 or 홀만 : +자 이동 0, 2, 4, 6
                    for k in range(0,8,2):
                        Fireballs.append([ay, ax, arrangedMass, arrangedSpeed, k])
            basket = []
        basket.append([by, bx, bm, bspeed, bdir])

    arrangedMass, arrangedSpeed= [sum(sp[ths] for sp in basket) for ths in range(2, 4)]
    isOdd=True
    isEven=True
    chk=1
    for Im,nt,using,these,dr  in basket:
        if not dr%2: # 짝수
            isOdd= False
        elif dr%2:
            isEven= False
    if not isEven and not isOdd:
        chk= 1
    else:
        chk= 0

    if len(basket) > 1:
        arrangedMass //= 5
        arrangedSpeed //= len(basket)
        if arrangedMass and chk: # 홀짝 같이있: x자 이동 1, 3, 5, 7
            for k in range(1,8,2):
                Fireballs.append([ay, ax, arrangedMass, arrangedSpeed, k])

        elif arrangedMass: # 짟 : +자 이동 0, 2, 4, 6
            for k in range(0,8,2):
                Fireballs.append([ay, ax, arrangedMass, arrangedSpeed, k])
    elif len(basket)==1:
        Fireballs.append(basket[0])

for t in range(1,K+1):
    new = []
    move(Fireballs, new)
    if not new:
        break
    Fireballs = []
    spreadifConverged(new, Fireballs)

ans = 0

for shot in Fireballs:
    ans += shot[2]
print(ans)


'''
50 2 1000
1 1 10 1 7
50 50 10 1 3
'''