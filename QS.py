from random import*
data = list(range(1,11))
shuffle(data)
print(data)
def QS(L,first,last):
    print(first,last)
    if first>=last:
        return []
    p = L[first]
    A = []
    B = []
    M = [p]
    for i in range(first+1,last+1):
        if L[i]<p:
            A.append(L[i])
        elif L[i]>p:
            B.append(L[i])
        else:
            M.append(L[i])

    for idx, i in enumerate(range(first,first+len(A))):
        L[i] = A[idx]
    for idx, i in enumerate(range(first+len(A),first+len(A)+len(M))):
        L[i] = M[idx]
    for idx, i in enumerate(range(first+len(A)+len(M),last+1)):
        L[i] = B[idx]
        
    QS(L,first,first+len(A)-1) # first부터 len(A)개: first, first+len(A)+1 7부터 5개: 7+5-1
    QS(L, first+len(A)+len(M), last) # 앞에꺼 이상부터

QS(data,0,9)
print(data)
        