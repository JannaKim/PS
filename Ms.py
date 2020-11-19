from random import*
data = list(range(10))
shuffle(data)

# merge sort

def merge(L, first, last):
    m = (first+last)//2
    i = first
    j = m+1
    B = []
    while i<m+1 and j<last+1:
        if L[i]<=L[j]:
            B.append(L[i])
            i+=1
        elif L[i]>=L[j]:
            B.append(L[j])
            j+=1
    for k in range(i,m+1):
        B.append(L[k])
    for k in range(j,last+1):
        B.append(L[k])

    for idx,i in enumerate(range(first,last+1)):
        L[i] = B[idx]




def MS(L, first, last):
    if first>=last:
        return
    m = (first+last)//2
    MS(L, first,m)
    MS(L, m+1, last)
    merge(L,first,last)

MS(data,0,9)
print(data)
