L=[0]+[int(input()) for _ in range(9)]


def f(first, last):
    if first>=last:
        return first
    elif first+1==last:
        if L[last]>L[first]:
            return last
        else:
            return first
    m=(first+last)//2
    A = f(first,m)
    B = f(m+1,last)
    if L[A]>L[B]:
        return A
    else:
        return B
ans=f(1,9)
print(L[ans], ans,sep='\n')

'''
3
29
38
12
57
74
40
85
61
8
'''