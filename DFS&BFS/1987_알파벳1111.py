R, C = map(int, input().split())
mp=[]
mp.append(' '*(C+2))
for _ in range(R):
    mp.append(' '+input()+' ')
mp.append(' '*(C+2))

dx=[0,0,1,-1]
dy=[1,-1,0,0]
mx=0
Q=[(1,1,mp[1][1])]
while Q:
    i,j,string=Q.pop()
    mx=max(mx,len(string))
    if mx==26:
        break
    
    for x, y in zip(dx,dy):
        if mp[i+x][j+y]!=' ' and mp[i+x][j+y] not in string:
            Q.append((i+x,j+y,string+mp[i+x][j+y]))
   

print(mx)