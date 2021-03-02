import sys; input= lambda: sys.stdin.readline().rstrip()
n= int(input())
m= int(input())
mp= [[1e9]*n for _ in range(n)]
for _ in range(m):
    a, b, c=[int(i)-1 for i in input().split()]
    c+=1
    mp[a][b]=min(mp[a][b],c)
for i in range(n):
    mp[i][i]=0

for i in range(n):
    for j in range(n):
        for k in range(n):
            if j!=k:
                mp[j][k]= min(mp[j][k], mp[j][i]+mp[i][k])

for i in range(n):
    for j in range(n):
        print([mp[i][j],0][mp[i][j]==1e9], end=' ')
    print()