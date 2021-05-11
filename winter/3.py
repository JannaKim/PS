def solution(maps, p, r):
    n= len(maps[0])
    m= n//2
    if n%2:
        m+=1
    L= [[100]*(n+2*m) for _ in range(m)]
    L+= [[100]*m +el+[100]*m for el in maps]
    L+= [[100]*(n+2*m) for _ in range(m)]
    print(len(L))
    [print(*el) for el in L]
    #
    M= len(L)
    side= r//2
    ans=0
    for i in range(m-1,m-1+n):
        for j in range(m-1,m-1+n):
            print(i,j)
            mp= [el[:] for el in L]
            #print(mp[9][4])
            ans=max(ans, draw(i,j,mp,side,p,n))

    return ans

def draw(y, x, mp, side,at,n):
    att= float(at)/2
    s=0
    oy, ox= y, x
    for _ in range(side):
        #print(y,x)
        if float(mp[y][x])<=att:
            s+=1
        mp[y][x]=0
        y-=1
        x+=1
    #print(y,x)
    y+=1
    for _ in range(side):
        #print(y,x)
        if float(mp[y][x])<=att:
            s+=1
        mp[y][x]=0
        y+=1
        x+=1
    #print(y,x)
    x-=1
    for _ in range(side):
        #print('?',y,x)
        if float(mp[y][x])<=att:
            s+=1
        mp[y][x]=0
        #print(y,x)
        y+=1
        x-=1
    #print(y,x)
    y-=1
    for _ in range(side):
        #print(y,x)
        if float(mp[y][x])<=att:
            s+=1
        mp[y][x]=0
        y-=1
        x-=1
    if side!=1:
        s+=dfs(oy, ox+1, mp,at ,n)
    #print(y,x)
    return s
Dy=[0,0,1,-1]
Dx=[1,-1,0,0]
def dfs(y, x, mp, at,n):
    ans=0
    for dy, dx in zip(Dy, Dx):
        ny= y+dy
        nx= x+dx
        if 0<=ny<n and 0<=nx<n and mp[ny][nx]:
            if mp[ny][nx]<=at:
                ans+=1
                mp[ny][nx]=0
                ans+=dfs(ny, nx, mp, at,n)
    return ans






print(solution([[1, 28, 41, 22, 25, 79, 4], [39, 20, 10, 17, 19, 18, 8], [21, 4, 13, 12, 9, 29, 19], [58, 1, 20, 5, 8, 16, 9], [5, 6, 15, 2, 39, 8, 29],[39, 7, 17, 5, 4, 49, 5], [74, 46, 8, 11, 25, 2, 11]]
,19,6))


#draw(2, 0, [[0]*6 for _ in range(6)],3,float(19)/2)


