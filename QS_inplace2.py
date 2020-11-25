import sys
sys.setrecursionlimit(500000)
N = int(input())
L = [int(input()) for _ in range(N)]

def merge(L, first, last):
    m = (first+last)//2
    i=first
    j=m+1
    A=[]
    while i<m and j<last:
        if L[i]<=L[j]:
            A.append(L[i])
            i+=1
        else:
            A.append(L[j])
            j+=1
    for k in range(i,m+1):
        A.append(L[i])
    for k in range(j,last+1):
        A.append(L[j])
    for i in range(first,last):
        L[i] = L[first,i]
        
def ms(L,first,last):
    if first>=last:
        return
    m=(first+last)//2
    ms(L,first,m)
    ms(L,m+1,last)
    merge(L,first,last)
print(L)