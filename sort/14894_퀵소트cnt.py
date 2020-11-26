# not inplace QS
N = int(input())
L=[int(i) for i in input().split()]
cnt=0
def QS(L):
    global cnt
    LEN = len(L)
    if LEN<=1:
        return L
    p = L[(LEN-1)//2]
    A, M, B= [], [], []
    for i in range(LEN):
        cnt+=1
        if L[i]<p:
            A.append(L[i])
        elif L[i]>p:
            B.append(L[i])
        else:
            M.append(L[i])
    
    
    return QS(A)+M+QS(B)
QS(L)
print(cnt)



