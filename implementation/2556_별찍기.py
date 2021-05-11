n =int(input())
n-=1
m= 2*n+1
mp= [[' ']*m for _ in range(m)]

base= [n,n]
for i in range(m):
    for j in range(m):
        if abs(i-base[0])+abs(j-base[1])==n:
            mp[i][j]='*'
[print(*el) for el in mp]
'''
for i in range(m):
    flag=False
    for j in range(m):
        if not flag and mp[i][j]=='*':
            flag=True
        if flag and mp[i][j]==' ':
            break
        print(mp[i][j],end='')
    print()
'''