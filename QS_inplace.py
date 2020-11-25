import sys
sys.setrecursionlimit(10000)
N = int(input())
L = [int(input()) for _ in range(N)]
def QS(X, a,b):
    if a>=b:
        return
    p = X[a]
    i = a+1
    j = b
    while i<=j:
        while i<=b and X[i]<=p:
            i+=1
        while X[j]>p:
            j-=1
        if i<j:
            X[i], X[j] = X[j], X[i]
            i+=1
            j-=1
    one=X[j]
    two=X[a]
    X[j], X[a] = two, one
    
    if a<j-1:
        QS(X,a,j-1)
    if i<b:
        QS(X,i,b)
QS(L, 0,N-1)
[print(i) for i in L]

'''
5
5
2
3
4
1
'''