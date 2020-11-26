N = int(input())
L = [int(input()) for _ in range(N)]

def qs(L,first,last):
    if first>=last:
        return
    p = L[last]
    i=first
    j=last-1
    while i<=j:
        while L[i]<p:
            i+=1
        while j>=first and L[j]>=p:
            j-=1
        if i<=j:
            L[i], L[j] = L[j], L[i]
            i+=1
            j-=1
        L[last], L[i]= L[i], L[last]

        qs(L,first,i-1)
        qs(L,i+1,last)
        
    
    

qs(L,0,N-1)
[print(i) for i in L]