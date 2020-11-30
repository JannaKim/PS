from math import log
N = int(input())
A = [int(i) for i in input().split()]
M = int(input())
B = [int(i) for i in input().split()]

def find(first, last,el):
    if first>last:
        return -1
    
    while first<last:
        m = (first+last)//2
        if A[m]<el:
            first=m+1
        elif A[m]>el:
            last=m-1
        else:
            return 1
    if A[first]==el:
        return 1
    else:
        return 0
'''
def f(el,d):
    return (el//10**d)%10

def radix_sort(L,d):
    C=[0]*10
    B=[-1]*len(L)
    for el in L:
        C[f(el,d)]+=1
    for i in range(1,10):
        C[i]+=C[i-1]
    for i in reversed(range(len(L))):
        B[C[f(L[i],d)]-1]=L[i]
        C[f(L[i],d)]-=1
    return B
        


def radix(L):
    digit = int(log(max(L),10))
    for d in range(digit+1):
        ans=radix_sort(L,d)
    return ans
A = radix(A)
'''
A.sort()
[print(find(0,N-1,el)) for el in B]

'''
5
4 1 5 2 3
5
1 3 7 9 5
'''