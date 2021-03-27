n= int(input())

for i in range(1,n+1):
    if i==n:
        print('*'*(2*n-1))
    elif i==1:
        print((n-1)*' '+'*')
    else:
        s= (n-i)*' '+'*'+' '*(i-1)
        t=' '*(i-2)+'*'
        print(s+t)