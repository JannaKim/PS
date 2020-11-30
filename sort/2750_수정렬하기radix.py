from math import log
N = int(input())
pos=[]
neg=[]
for _ in range(N):
    num = int(input())
    if num>=0:
        pos.append(num)
    else:
        neg.append(-num)


def f(num,d):
    return (num//10**d)%10

def radix_sort(L,d):
    C=[0]*10
    B=[-1]*len(L)
    for el in L: # 0~9
        C[f(el,d)]+=1

    for i in range(9):
        C[i+1]+=C[i] # rank


    for i in reversed(range(len(L))):
        B[C[f(L[i],d)]-1]=L[i] # 같은값들을 제 자리에 유지하도록 정렬해주기 위해
        # reversed
        # 알파벳 
        # log  3배정도 log10n log2n
        # 53 52 
        # 52 53
        # 2 2
        # 0 1
        # 52 53

    
        C[f(L[i],d)]-=1


    return B # 안하면? L=B[:] 작업이 없다.

def radix(L):
    if not len(L):
        return
    digit = int(log(max(L), 10))

    for d in range(digit+1):
        L = radix_sort(L,d)
    return L

neg=radix(neg)
pos=radix(pos)
ans=([-i for i in neg[::-1]] if neg else [])+(pos if pos else [])
[print(i) for i in ans]

# 5 3 5 8 9 7 9
