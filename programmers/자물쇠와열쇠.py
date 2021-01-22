r=range
def solution(key, lock):
    lockLen= len(lock[0])
    fakeLen=lockLen+2*(lockLen-1)
    mp=[]
    mp=[[-1]*(fakeLen+2)]
    mp+=[[-1]+[0]*fakeLen+[-1] for _ in r(lockLen-1)]
    for i in r(lockLen):
        mp+=[[-1]+[0]*(lockLen-1)+lock[i]+[0]*(lockLen-1)+[-1]]
    mp+=[[-1]+[0]*fakeLen+[-1] for _ in r(lockLen-1)]
    mp+=[[-1]*(fakeLen+2)]
    [print(*el) for el in mp]

    realloc=(lockLen,lockLen)
    keyLen= len(key[0])
    # roof
    Rside= [[0]*keyLen for _ in r(keyLen)]
    floor= [[0]*keyLen for _ in r(keyLen)]
    Lside= [[0]*keyLen for _ in r(keyLen)]
    for i in r(keyLen):
        for j in r(keyLen):
            Rside[j][keyLen-1-i]= key[i][j]
            floor[keyLen-1-i][keyLen-1-j]= key[i][j]
            Lside[keyLen-1-j][i]= key[i][j]


    def tryopen(thiskey):
        for i in r(1,1+fakeLen):
            for j in r(1,1+fakeLen):
                for ki, row in enumerate(r(i,i+keyLen)):
                    if row>fakeLen: break
                    for kj, col in enumerate(r(j,j+keyLen)):
                        print(row,col)
                        if mp[row][col]<0:
                            break
                        mp[row][col]+=thiskey[ki][kj]
                checking=True
                for oi, a in enumerate(r(realloc[0],realloc[0]+lockLen)):
                    for oj, b in enumerate(r(realloc[1], realloc[1]+lockLen)):
                        if checking and mp[a][b]!=1:
                                checking=False
                        mp[a][b]=lock[oi][oj]
                if checking: return True
        return False
    if tryopen(key) or tryopen(Rside) or tryopen(floor) or tryopen(Lside):
        return True
    
    return False
