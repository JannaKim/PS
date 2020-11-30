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
        if i<=j: # j i
            L[i], L[j] = L[j], L[i]
            i+=1
            j-=1 
    '''
    i j 마지막 위치
    1) j+1=i 일 때, i, j 같은 위치일 때 L[i]!=p일때

    2) j+2=i 일 때, i, j 같은 위치일 때 L[i]==p일때

    왼쪽끝~ j의 마지막 위치: p보다 작은 el
    i의 마지막 위치~오른쪽 끝: p보다 큰 el

    '''
    
    print(L[first:i])
    print(L[i:last+1]) # i는 p작거나 같은애들만 있음 j도 p보다 크거나 같은애들만 있음
    QS(L,first,i-1) # i기준으로 나뉨 
    QS(L,i,last) # 왜 i?
QS(L,0,N-1)

def qs(L,first,last):
    if first>=last:
        return
    p = first
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