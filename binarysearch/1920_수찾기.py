from sys import *
input = lambda: stdin.readline().rstrip()

N = int(input())
*L, = map(int, input().split())
L.sort()
M = int(input())
*chk, = map(int, input().split())

def BS(a, b, c):
    if b-a<=1:
        if L[b]==c:
            return 1
        elif L[a]==c:
            return 1
        else:
            return 0
    m = (a+b)//2
    if L[m]>c:
        return BS(a,m-1,c)
    elif L[m]<c:
        return BS(m+1,b,c)
    else:
        return 1
for el in chk:
    print(BS(0, N-1, el))