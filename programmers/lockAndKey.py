r= range
enum= enumerate
def solution(key, lock):
    N= len(lock[0])
    M= len(key[0])

    # lock size
    ulL=urL=dlL=drL=0
    for i in r(N):
        for j in r(N):
            if not lock[j][i]:
                ulL=(j,i)
                break
    for i in r(N-1, -1, -1):
        for j in r(N):
            if not lock[j][i]:
                urL=(j,i)
                break
    for i in r(N):
        for j in r(N-1,-1,-1):
            if not lock[j][i]:
                dlL= (j,i)
                break
    for i in r(N-1,-1,-1):
        for j in r(N-1,-1,-1):
            if not lock[j][i]:
                drL= (j,i)
                break
    #print(ulL, urL, dlL, drL)
    startL= (min(ulL[0], urL[0], dlL[0], drL[0]), min(ulL[1],urL[1],drL[1], dlL[1]))
    endL= (max(ulL[0], urL[0], dlL[0], drL[0]), max(ulL[1],urL[1],drL[1], dlL[1]))
    dL= endL[0]- startL[0]+1
    wL= endL[1]- startL[1]+1

    

    # key size
    ulK=urK=dlK=drK=0
    for i in r(N):
        for j in r(N):
            if key[j][i]:
                ulK=(j,i)
                break
    for i in r(N-1, -1, -1):
        for j in r(N):
            if key[j][i]:
                urK=(j,i)
    for i in r(N):
        for j in r(N-1,-1,-1):
            if key[j][i]:
                dlK= (j,i)
    for i in r(N-1,-1,-1):
        for j in r(N-1,-1,-1):
            if key[j][i]:
                drK= (j,i) 
    startK= (min(ulK[0], urK[0], dlK[0], drK[0]), min(ulK[1],urK[1],drK[1], dlK[1]))
    endK= (max(ulK[0], urK[0], dlK[0], drK[0]), max(ulK[1],urK[1],drK[1], dlK[1]))
    dK= endK[0]- startK[0]+1
    wK= endK[1]- startK[1]+1

    #print(f'startL {startL}')
    #print(f'endL {endL}')
    #print(f'startK {startK}')
    #print(f'endK {endK}')
    sum=0
    #roof
    for x, i in enum(r(startK[0], startK[0]+dL)):
        for y, j in enum(r(startK[1], startK[1]+wL)):
            #print(f'lock[{x+startL[0]}][{y+startL[1]}]==key[{i}][{j}]')
            sum+=(1 if lock[x+startL[0]][y+startL[1]]^1==key[i][j] else 0)
    #print(f'sum {sum}')
    if sum==dL*wL: return True

    sum=0
    #left side
    for x, i in enum(r(startK[1], startK[1]+wL)):
        for y, j in enum(r(startK[0]+dL-1, startK[0]-1,-1)):
            #print(f'lock[{x+startL[0]}][{y+startL[1]}]==key[{j}][{i}]')
            sum+=(1 if lock[x+startL[0]][y+startL[1]]^1==key[j][i] else 0)
    #print(f'sum {sum}')
    if sum==dL*wL: return True

    sum=0
    #right side
    for x, i in enum(r(startK[1]+wK-1, startK[1]+wK-1-dL,-1)):
        for y, j in enum(r(startK[0], startK[0]+dL)):
            #print(f'lock[{x+startL[0]}][{y+startL[1]}]==key[{j}][{i}]')
            sum+=(1 if lock[x+startL[0]][y+startL[1]]^1==key[j][i] else 0)
    #print(f'sum {sum}')
    if sum==dL*wL: return True

    sum=0
    #floor
    for x, i in enum(r(startK[0]+dK-1, startK[0]+dK-1-dL,-1)):
        for y, j in enum(r(endK[1], endK[1]-wL,-1)):
            #print(i,j)
            #print(f'lock[{x+startL[0]}][{y+startL[1]}]==key[{i}][{j}]')
            sum+=(1 if lock[x+startL[0]][y+startL[1]]^1==key[i][j] else 0)
    #print(f'sum {sum}')
    if sum==dL*wL: return True

    return False

solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]])

