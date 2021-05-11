n= int(input())
m= 2*n-1
mp=[[' ']*m for _ in range(n)]
y, x= 0,n-1
for i in range(n):
    for j in range(m):
        if abs(i-y)+abs(j-x)<=n-1:
            mp[i][j]='*'

ends=[0]*n
for i in range(n):
    for j in range(m-1,-1,-1):
        if mp[i][j]=='*':
            ends[i]=j
            break

for i in range(n):
    for j in range(m):
        print(mp[i][j],end='')
        if ends[i]==j:
            break
    print()
