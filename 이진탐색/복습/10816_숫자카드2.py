import sys
sys.setrecursionlimit(500000)
N = int(input())
L = [int(i) for i in input().split()]

def merge(L, first, last):
    m = (first+last)//2
    i=first
    j=m+1
    A=[]
    while i<=m and j<=last:
        if L[i]<=L[j]:
            A.append(L[i])
            i+=1
        else:
            A.append(L[j])
            j+=1
    for k in range(i,m+1):
        A.append(L[k])
    for k in range(j,last+1):
        A.append(L[k])
    for i in range(first,last):
        L[i] = A[first-i]
        
def ms(L,first,last):
    if first>=last:
        return
    m=(first+last)//2
    ms(L,first,m)
    ms(L,m+1,last)
    merge(L,first,last)
ms(L,0,N-1)
print(L)

'''
10
6 3 2 10 10 10 -10 -10 7 3

5
5
2
3
4
1
'''