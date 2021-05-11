n= int(input())
n=2*n-1
m=2*n-1
mp=[[' ']*m for _ in range(m)]
for i in range(m//2+1):
    for j in range(i,i+m-i*2):
        for k in range(i,i+m-i*2):
            if not i%2:
                mp[j][k]='*'
            else:
                mp[j][k]=' '
for i in range(m):
    print(''.join(mp[i]))
