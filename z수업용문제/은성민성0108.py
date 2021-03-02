import sys
sys.setrecursionlimit(25000)
T=int(input())
for _ in range(T):
    garo, selo, getsoo = [int(i) for i in input().split()]
    #M: 가로

    mp=[]

    for i in range(selo):
        mp.append([0]*garo)


    for __ in range(getsoo):
        X,Y = [int(i) for i in input().split()]
        mp[Y][X]=1

    feild=[]
    feild.append([0]*( garo +2))   

    for l in range(0,selo):
        feild.append([0]+mp[l]+[0])  
    feild.append([0]*( garo +2))      

    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    answer=0
    def f(a,b):
        feild[a][b]=0
        for x,y in zip(dx,dy):
            if feild[a+x][b+y]:
                f(a+x,b+y)

    # f는 현제 좌표를 포함해서 붙어있는 모든 1을 0으로 바꾸는 함수 
    for o in range(0, selo+2):
        print(*feild[o])

    for i in range(1,selo+1): # range 안붙여줌
        for j in range(1,garo+1):
            print(i,j)
            if feild[i][j]==1:
                f(i,j)
                answer=answer+1
    print (answer)


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