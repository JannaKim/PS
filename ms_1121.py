L = [4,1,5,9,2,6,5]

def merge(L, first, last):
    m = (first+last)//2

    i = first
    j = m+1
    A = []
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
        L[i] = A[i-first]





def ms(L,first,last):
    if first>=last:
        pass
    else:
        m = (first+last)//2
        ms(L, first,m)
        ms(L,m+1,last)
        merge(L,first,last)

ms(L,0,len(L)-1)
print(L)