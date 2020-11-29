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
    for el in L:
        C[f(el,d)]+=1
    for i in range(9):
        C[i+1]+=C[i]
    for i in reversed(range(len(L))):
        #print(f'B[C[{f(L[i],d)}]-1]=L[i]')
        #print(f'B[{C[f(L[i],d)]}-1]=L[i]')
        B[C[f(L[i],d)]-1]=L[i]
        C[f(L[i],d)]-=1
    return B # 안하면? L=B[:] 작업이 없다.
def radix(L):
    if not len(L):
        return
    digit = int(log(max(L), 10))
    ans=[]
    for d in range(digit+1):
        ans = radix_sort(L,d)
    return ans

neg=radix(neg)
pos=radix(pos)
ans=([-i for i in neg[::-1]] if neg else [])+(pos if pos else [])
[print(i) for i in ans]
