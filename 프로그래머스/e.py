def solution(v):   
    N = len(v[0]) 

    mp = [[-1]*(N+2)]

    for line in v:
        mp.append([-1]+ line + [-1])
    mp.append([-1]*(N+2))


    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    def f(a,b,v):
        mp[a][b]=-1
        for x,y in zip(dx,dy):
            if mp[a+x][b+y]==v:
                f(a+x,b+y,v)

    ans = [0]*3
    for i in range(1,N+1):
        for j in range(1,N+1):
            if mp[i][j]!=-1:
                ans[mp[i][j]]+=1
                f(i,j,mp[i][j])
                

    
    return ans
    

solution([[0,0,1,1],[1,1,1,1],[2,2,2,1],[0,0,0,2]])