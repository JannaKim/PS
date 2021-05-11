n= int(input())
r=2*n-1
c=n
y, x= n-1,n-1
for i in range(r):
    for j in range(c):
        if abs(y-i)+abs(x-j)<=n-1:
            print('*',end='')
        else:
            print(' ',end='')
    if i!=r-1:
        print()