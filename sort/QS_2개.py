from random import*
N = int(input())
L = [int(input()) for _ in range(N)]
M = L[:]
def QS(L, first, last):
    if first>=last:
        return
    p = L[randint(first,last)]
    i=first
    j=last

    while i<=j:
        while L[i]<p:
            i+=1
        while L[j]>p:
            j-=1
        if i<=j:
            L[i], L[j] = L[j], L[i]
            i+=1
            j-=1
    
    QS(L,first,i-1)
    QS(L,i,last)
QS(L,0,N-1)

def qs(L,first,last):
    if first>=last:
        return
    p = randint(first,last)
    i=first+1
    j=last
    while i<=j:
        while i<=last and L[i]<=L[p] or i==p:
            i+=1
        while j<=first+1 and L[j]>L[p] or i==p:
            j-=1
        if i<j:
            L[i], L[j] = L[j], L[i]
    L[p], L[j] = L[j], L[p]
    qs(L,first,j-1)
    qs(L,j+1,last)
QS(M,0,N-1)
[print(i) for i in M]
print(L,M,end='\n')