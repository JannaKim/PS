import sys
sys.setrecursionlimit(500000)
N = int(input())
L = [int(input()) for _ in range(N)]

def qs(L, first, last):
    if first>=last:
        return
    p = L[(first+last)//2]
    i = first
    j = last
    while i<=j:
        while L[i]<p:
            i+=1
        while L[j]>p:
            j-=1
        
        if i<=j:
            a, b = L[i], L[j]
            L[i], L[j] = b, a
            i+=1
            j-=1
    qs(L,first,i-1)
    qs(L,i,last)


qs(L, 0,N-1)
[print(i) for i in L]