n= int(input())

m= n*4-2
mp=[[' ']*m for _ in range(2*n-1)]
c= m
r= 2*n-1
y,x=0,0
for i in range(n):
    mp[y][x]='*'
    x+=1
x-=1
for i in range(2*n-1):
    mp[y][x]='*'
    x+=1
    y+=1
x-=1
y-=1
for i in range(n):
    mp[y][x]='*'
    x+=1
x-=1
for i in range(n):
    mp[y][x]='*'
    x-=1
    y-=1
x+=1
y+=1
for i in range(n):
    mp[y][x]='*'
    x+=1
    y-=1
x-=1
y+=1
for i in range(n):
    mp[y][x]='*'
    x-=1
x+=1
for i in range(2*n-1):
    mp[y][x]='*'
    x-=1
    y+=1
x+=1
y-=1
for i in range(n):
    mp[y][x]='*'
    x-=1
x+=1
for i in range(n):
    mp[y][x]='*'
    x+=1
    y-=1
x-=1
y+=1
for i in range(n):
    mp[y][x]='*'
    x-=1
    y-=1


#[print(*el) for el in mp]

ends=[]
for i in range(r):
    for j in range(c-1,-1,-1):
        if mp[i][j]=='*':
            ends.append(j)
            break

for i in range(r):
    for j in range(c):
        print(mp[i][j],end='')
        if ends[i]==j:
            break
    print()