n , m , R= map(int, input().split())
mp = [ [*map(int, input().split())] for _ in range(n)]


chk = [[False] * m for _ in range(n)]
loy , lox , hiy , hix = 0 , 0 , n - 1 , m - 1
r , c = n , m
while r and c:
    #print(loy , hiy , lox , hix)
    rot = R % (2 * r + 2 * c - 4)
    #print(rot)
    E = []
    stc = []
    for i in range(n):
        for j in range(m):
            if not chk[i][j]:
                if i == loy or  j == hix:
                    chk[i][j] = True
                    stc.append( (i , j) )
                    E.append(mp[i][j])

    for i in range(n - 1 , -1 , -1):
        for j in range(m - 1 , -1 , -1):
            #print(i , j)
            if not chk[i][j]:
                if i == hiy or j == lox:
                    chk[i][j] = True
                    stc.append( (i , j) )
                    E.append(mp[i][j])
    #print(stc)
    #print(E)
    ln = len(stc)
    stc = stc[:] + stc[:]
    stc = stc[ln-rot : ln - rot + ln]
    #print(stc)
    for idx , (y , x) in enumerate(stc):
        mp[y][x] = E[idx]
    loy , lox , hiy , hix = loy + 1 , lox + 1 , hiy - 1 , hix -1
    r -= 2
    c -= 2
#print()
[print(*el) for el in mp]

'''
4 2 1
1 2
5 6
9 10
13 14

5 4 14
1 2 3 4
7 8 9 10
13 14 15 16
19 20 21 22
25 26 27 28

3 2 3 2 -4 6
'''
