T = int(input())

dx = [0,0,1,-1]
dy = [1,-1,0,0]
for _ in range(T):
    M, N, K = [int(i) for i in input().split()]
    #M: 가로

    mp=[]
    for i in range(N+2):
        mp.append([0]*(M+2))

    [print(i) for i in mp]   
    for _ in range(K):
        X,Y = [int(i) for i in input().split()]
        mp[Y+1][X+1]=1
    [print(i) for i in mp]

    def f(a,b):
        mp[a][b]=0
        for x,y in zip(dx,dy):
            if mp[a+x][b+y]:
                f(a+x,b+y)
    print()
    cnt=0
    for i in range(1,N+1):
        for j in range(1,M+1):
            print(i,j)
            if mp[i][j]==1:
                f(i,j)
                cnt+=1
    [print(i) for i in mp]
    print(cnt)

'''
10 8 17
0 0
1 0
1 1
4 2
4 3
4 5
2 4
3 4
7 4
8 4
9 4
7 5
8 5
9 5
7 6
8 6
9 6
'''