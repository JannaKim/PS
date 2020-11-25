from sys import *
setrecursionlimit(500000)
input = lambda: stdin.readline().rstrip()
N = int(input())
L = [int(i) for i in input().split()]
M = int(input())
C = [int(i) for i in input().split()]
'''
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
    for i in range(first,last+1):
        L[i] = A[first-i]
        
def ms(L,first,last):
    if first>=last:
        return
    m=(first+last)//2
    ms(L,first,m)
    ms(L,m+1,last)
    merge(L,first,last)
ms(L,0,N-1)
'''

def left(L,k): # 첫 k에 가는 게 목표였는데 k가 없다면 더 작은 곳에 가있을것

    i, j = 0,N-1
    while i<j:
        m = (i+j)//2
        if L[m]<k:
            i=m+1
        else:
            j=m
    if L[i]<k:
        return i+1
    return i

def right(L,k): # k앞에 가는 게 목표인데 k가 인덱스의 마지막에 있었다면 k에 가있을것
    i, j = 0,N-1
    while i<j:
        m=(i+j)//2
        if L[m]<=k:
            i=m+1
        else:
            j=m
    if L[i]<=k:
        return i+1
    return i

L.sort()

ans=[]
for el in C:
    a = left(L,el)
    b = right(L,el)
    ans.append(b-a)
print(*ans)



'''
10
6 3 2 10 10 10 -10 -10 7 3
8
10 9 -5 2 3 4 5 11


2
1 2
8  
0 1 0 1 2 3 4 5   
'''