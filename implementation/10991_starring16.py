n= int(input())
n+=1
c= 2*n-1
y, x= n-1,n-1
mp=[[' ']*c for _ in range(n)]
for i in range(n):
    for j in range(c):
        ths=abs(y-i)+abs(x-j)
        if ths<=n-1 and ths%2==n%2:
            mp[i][j]='*'
ends=[0]*n
for i in range(n):
    for j in range(c-1,-1,-1):
        if mp[i][j]=='*':
            ends[i]=j
            break

for i in range(1,n):
    for j in range(1,c):
        print(mp[i][j],end='')
        if ends[i]==j:
            break
    if i!=n-1:
        print()