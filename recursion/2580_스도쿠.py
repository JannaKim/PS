import sys; input= lambda: sys.stdin.readline().rstrip()
mp= [[*map(int, input().split())] for _ in range(9)]

def fill(i, j):
    found= False
    while i<=8 and j<=8:
        if not mp[i][j]:
            found=True
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
            for t in range(1,10):
                if not chk[t]:
                    mp[i][j]=t
                    nxt_j= j+1
                    nxt_i= i+(j+1)//9
                    nxt_j%=9
                    fill(nxt_i, nxt_j)
                    mp[i][j]=0 # 이거 안해주면 갈아엎기 안됨
            break
        j+=1
        i+=j//9
        j%=9
    if not found: # (9,0) 까지 도달 못해면 다 채웠어도 출력안함
        [print(*el) for el in mp]
        exit()


fill(0,0)
'''
1 3 5 4 6 9 2 7 8
7 0 2 1 0 5 6 0 9
4 6 9 2 7 8 1 3 5
3 2 1 5 4 6 8 9 7
8 0 4 9 0 3 5 0 6
5 9 6 8 2 7 4 1 3
9 1 7 6 5 2 3 8 4
6 0 3 7 0 1 0 0 0
2 5 8 3 9 4 0 0 0
'''