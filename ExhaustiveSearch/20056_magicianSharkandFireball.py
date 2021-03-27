from collections import deque
dy= [-1, -1, 0, 1, 1, 1, 0, -1]
dx= [0, 1, 1, 1, 0, -1, -1, -1]


n, m, K= map(int, input().split())
sharks = []
for _ in range(m):
    r, c, m, s, d=  map(int, input().split()) # 합질량, 합속력, 합방향, 합쳐진 개수
    sharks.append([r-1,c-1,m,s,d])

def move(tmp, new): # 하나만
    for i, j, mass, speed, direct in tmp:
        ny= (i+dy[direct]*speed+n)%n
        nx= (j+dx[direct]*speed+n)%n
        new.append([ny, nx, mass, speed, direct])
        #print(ny, nx,mass,speed)

def spread(tmp, sharks):
    tmp.sort()
    spreads=[]
    ay, ax, am, aspeed, adir= tmp[0]
    by, bx, bm, bspeed, bdir= [0,0,0,0,0]
    spreads.append([ay, ax, am, aspeed, adir])
    #print('is it spreadable?',tmp)
    for a, b in zip(tmp, tmp[1:]):
        #print('spreads',spreads)
        #print(a,b)
        ay, ax, am, aspeed, adir= a
        by, bx, bm, bspeed, bdir= b
        if ay!=by or ax!=bx:
            #print(ay, ax, by, bx)
            if len(spreads)==1:
                sharks.append(spreads[0])
            else:
                #print('ㅇㅇ',spreads,len(spreads))
                mass, speed, direct= [sum(spread[k] for spread in spreads) for k in range(2, 5)]
                
                mass //= 5
                #print('spreads len',len(spreads))
                #print(spreads)
                speed //= len(spreads)
                #print(speed,mass)
                #if mass: # 소멸

                if mass and direct%2: # 홀수: x자 이동 1, 3, 5, 7
                    for k in range(1,8,2):
                        sharks.append([ay, ax, mass, speed, k])

                elif mass: # 짟 : +자 이동 0, 2, 4, 6
                    for k in range(0,8,2):
                        sharks.append([ay, ax, mass, speed, k])
            spreads = []
        spreads.append([by, bx, bm, bspeed, bdir])
        #print(spreads)
    #print('last?',spreads)

    mass, speed, direct= [sum(spread[k] for spread in spreads) for k in range(2, 5)]
    if len(spreads) > 1:
        mass //= 5
        speed //= len(spreads)
        if mass<1: # 소멸
            return
        if direct%2: # 홀수: x자 이동 1, 3, 5, 7
            for k in range(1,8,2):
                sharks.append([ay, ax, mass, speed, k])

        else: # 짟 : +자 이동 0, 2, 4, 6
            for k in range(0,8,2):
                sharks.append([ay, ax, mass, speed, k])
    else:
        sharks.append(spreads[0])
    #print('spreaded if mendatory',print(sharks))
for t in range(1,K+1):
    new = []
    move(sharks, new)
    sharks = []
    spread(new, sharks)
    #print(f't {t} over')
ans = 0

for shark in sharks:
    ans += shark[2]
print(ans)

'''
50 2 1000
1 1 10 1 7
50 50 10 1 3