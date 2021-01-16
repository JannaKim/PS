import sys
sys.setrecursionlimit(25000)
T = int(input())
for _ in range(T):
    garo, sero, K = [int(i) for i in input().split()]
    #M: 가로

    mp=[]
    field = []
    answer=0
    for i in range(sero):
        mp.append([0]*(garo))

    for _ in range(K):
        X,Y = [int(i) for i in input().split()]
        mp[Y][X]=1

    field.append([0]*(garo+2))
    for i in range(0, sero):
        field.append([0]+mp[i]+[0])
    field.append([0]*(garo+2))


    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    def f(a,b):
        field[a][b]=0
        for x,y in zip(dx,dy):
            if field[a+x][b+y]:
                f(a+x,b+y)
    #f = 지금 현제 좌표를 포함하여 붙어있는 모든 1을 0으로 바꾸는 함수

    #[print(*i) for i in field]
    for i in range(1,sero+1):
        for j in range(1,garo+1):
            if field[i][j]==1:
                f(i, j)
                answer+=1
    print(answer)