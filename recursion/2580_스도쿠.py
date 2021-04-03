import sys; input= lambda: sys.stdin.readline().rstrip()

mp= [[*map(int, input().split())] for _ in range(9)]


def fill(i, j):
    if (i, j)==(9, 0):
        [print(*el) for el in mp]
        exit()

    while i<=8 and j<=8:
        if not mp[i][j]:
            chk= [True]+[False]*9
            for k in range(9):
                chk[mp[i][k]]=True
            for k in range(9):
                chk[mp[k][j]]=True
            a= i-i%3
            b= j-j%3
            for y in range(a, a+3):
                for x in range(b, b+3):
                    chk[mp[y][x]]=True
            #print(R, C, B, sep='\n')
            for t in range(1,10):
                if not chk[t]:
                    mp[i][j]=t
                    #[print(*el) for el in mp]
                    #print()
                    nxt_j= j+1
                    nxt_i= i+(j+1)//9
                    nxt_j%=9
                    fill(nxt_i, nxt_j)
                    mp[i][j]=0
            break
        j+=1
        i+=j//9
        j%=9

fill(0,0)

