n, m= map(int, input().split())
L=[*map(int, input().split())]

mx= 100000*10000

def fit(k):
    tmp=k
    cnt=1
    for el in L:
        if tmp<el:
            cnt+=1
            tmp=k-el
        else:
            tmp-=el
    #print(cnt)
    return cnt

def bs():
    lo= max(L)
    hi=10000*100000
    ans=0
    while lo<hi:
        #print(lo,hi)
        mid= (lo+hi)//2
        if fit(mid)<=m:
            hi=mid
        else:
            lo=mid+1
    print(lo)
bs()