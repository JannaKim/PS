from math import log
N = int(input())

LEN = len(str(N))


first = N- 9*LEN

for i in range(first,N):
    digit = int(log(i,10))
    s=i
    for d in range(digit+1):
        d+=f(i,j)
    if s==N:
        print(i) 
        exit()
        break
    
'''
def f(n,d):
    return (n//10**d)%10

if N> 10**(LEN-1)+9*(LEN-1):
    for i in range(10**(LEN-1),N):
    #for i in range(1,N):
        digit = int(log(i,10))
        s = i
        for j in range(digit+1):
            s+=f(i,j)
        if s==N:
            print(i)
            exit()
            break

else:
    for i in range((10**(LEN-2) if LEN>=2 else 1),N):
    #for i in range(1,N):
        digit = int(log(i,10))
        s = i
        for j in range(digit+1):
            s+=f(i,j)
        if s==N:
            print(i)
            exit()
            break
print(0)
'''

        