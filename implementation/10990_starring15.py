n= int(input())
mp=[[' ']*n*2 for _ in range(n)]
y, x= n-1,0
for _ in range(n):
    mp[y][x]='*'
    y-=1
    x+=1
y+=1
x-=1
for _ in range(n):
    mp[y][x]='*'
    y+=1
    x+=1
ends=[0]*n
for i in range(n):
    for j in range(n*2-1,-1,-1):
        if mp[i][j]=='*':
            ends[i]=j
            break

for i in range(n):
    for j in range(n*2):
        print(mp[i][j],end='')
        if ends[i]==j:
            break
    print()