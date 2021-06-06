n , L , R = map(int , input().split())


Land = [ [*map(int , input().split())] for _ in range(n)]
Dy = [0,0,1,-1]
Dx = [1,-1,0,0]
Open = [ [False] * n for _ in range(n) ]
moved = [ [False] * n for _ in range(n) ] 

def bound(y , x):
    if 0 <= y < n and 0 <= x < n:
        return True
    return False

def open(y , x):
    global L , R
    cur = Land[y][x]

    for dy , dx in zip(Dy , Dx):
        ny = y + dy
        nx = x + dx
        if bound(ny , nx):
            cmp = Land[ny][nx]
            if L <= abs(cur - cmp) <= R:
                Open[y][x] = True
                Open[ny][nx] = True

def flood(y , x):
    loc = [(y , x)]
    sm , nm  = Land[y][x] , 1
    for dy , dx in zip(Dy , Dx):
        ny = y + dy
        nx = x + dx
        if bound(ny , nx) and not moved[ny][nx] and Open[ny][nx]:
            moved[ny][nx] = True
            forLOC, forSM , forNM = flood(ny , nx)
            loc += forLOC[:]
            sm += forSM
            nm += forNM

    return loc , sm , nm

for t in range(2002):
    Open = [ [False] * n for _ in range(n) ] #계속 초기화하기
    for i in range(n):
        for j in range(n):
            open(i , j)
    #[print(*el) for el in Open]
    moved = [ [False] * n for _ in range(n) ] 

    flag = False
    for i in range(n):
        for j in range(n): # open  된것 끼리 묶어서 이동시킹
            if not moved[i][j] and Open[i][j]:
                flag = True

                moved[i][j] = True
                union , s , num = flood(i , j) # 좌표 , 합 , 개수
                #print(union , s , num)
                united = s // num

                for y , x in union: # 이동시키기
                    Land[y][x] = united
                #[print(*el) for el in Land]
    
    if not flag:
        print(t)
        break
    #sleep(1)


'''
2 1 1
1 2
4 3
'''
