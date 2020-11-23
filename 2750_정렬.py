N = int(input())
L = [int(input()) for _ in range(N)]



def QS(X, a,b):
    if a>=b:
        return

    p = X[a]
    i = a+1
    j = b
    while i<=j:
        while i<=b and X[i]<p:
            i+=1
        while j>a and X[j]>=p:
            j-=1
        if i<=j:
            X[i], X[j] = X[j], X[i]
            i+=1
            j-=1

    X[j], X[a] = X[a], X[j]

    
    QS(X,a,j-1)
    QS(X,i,b)

QS(L,0,N-1)
[print(i) for i in L]