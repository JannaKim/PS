'''
n=int(input())
a=[]
for i in range (n-1):
    if i==0:
        print(' '*(n-i-1)+'*')
    else:
        print(' '*(n-i-1)+'*'+' '*((i-1)*2+1)+'*')

print('*'*(2*n-1))
'''
'''
A=[]
L=['_']*10
for i in range (10):
    A.append(L[:])
A[0][1]='*'



B=[]
for _ in range(2):
    B.append([el[:] for el in A])
B[0][0][0]='#'

# [[print(*el) for el in B[i]] for i in range(2)]
'''


n=int(input())
#가로,세로=2n-1,n
#중심-n,n
#거리=n-1
P=[]
a=[' ']*(2*n-1)
for i in range (n):
    P.append(a[:])
    '''
for _ in P:
    print(_)
    '''
for i in range (n):
    for q in range (2*n-1):
        if 