n= int(input())
r= n
c= 2*n-1
y, x= r-1,r-1
for i in range(r):
    for j in range(c):
        if abs(i-y)+abs(j-x)<=n-1:
            print('*'*(2*(i+1)-1))
            break
        else:
            print(' ',end='')