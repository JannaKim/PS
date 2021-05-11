n= int(input())
y, x= 0,n-1
for i in range(n):
    for j in range(n):
        if abs(i-y)+abs(j-x)<=n-1:
            print('*',end='')
        else:
            print(' ',end='')
    if i!=n-1:
        print()