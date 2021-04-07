mp= [[*map(int,list(input()))] for _ in range(9)]

def backtrack(i, j):
    flag=False
    while i<=8 and j<=8:
        if not mp[i][j]:
            flag=True
            chk=[False]*10
            for k in range(9):
                chk[mp[i][k]]=True
            for k in range(9):
                chk[mp[k][j]]=True
            a=i-i%3
            b=j-j%3
            for c in range(a,a+3):
                for d in range(b,b+3):
                    chk[mp[c][d]]=True
            for k in range(1,10):
                if not chk[k]:
                    mp[i][j]=k
                    nj=j+1
                    ni=i+j//9
                    nj%=9
                    backtrack(ni,nj)
                    mp[i][j]=0
            break # ?
        j+=1
        i=i+j//9
        j%=9
    if not flag:
        for y in range(9):
            for x in range(9):
                print(mp[y][x],end='')
            print()
        exit()

backtrack(0,0)