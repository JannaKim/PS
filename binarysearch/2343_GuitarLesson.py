n, m= map(int, input().split())
L=[*map(int, input().split())]

mx= 100000*10000


def record(blueray):
    cnt=1
    k=blueray
    for el in L:
        if el<=k:
            k-=el
        else:
            cnt+=1
            k=blueray-el
    return cnt

lo=max(L)
hi=mx
while lo<hi:
    mid= (lo+hi)//2
    if record(mid)<=m:
        hi= mid
        ans=mid
    elif record(mid)>m:
        lo= mid + 1
print(ans)