n= int(input())
for i in range(n):
    if not i%2:
        print('* '*(n-1)+'*')
    else:
        print(' *'*n)