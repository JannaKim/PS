n= int(input())
L=[*map(int, input().split())]
b= int(input())

lo=0
hi=b

def give(k):
    sm=0
    for el in L:
        if el>k:
            sm+=k
        else:
            sm+=el
    return sm
while lo+1<hi:
    mid= (lo+hi)//2
    if give(mid)>b:
        hi=mid-1
    else:
        lo=mid
ans=-1
if give(lo+1)<=b:
    for el in L:
        if el>lo+1:
            ans=lo+1
        else:
            ans=max(ans,el)
else:
    for el in L:
        if el>lo:
            ans=lo
        else:
            ans=max(ans,el)
print(ans)