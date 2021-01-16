import sys; sys.setrecursionlimit(100000)


n,m,k= map(int, input().split())


def fac(n):
    s=1
    for i in range(1,n+1):
        s*=i
    return s

def f(na, nz,cnt):
    if cnt==1:
        return 'a'*na+ 'z'*nz
    if na==0 and nz==1:
        return 'z'
    if na==1 and nz==0:
        return 'a'

    seq=fac(na-1+nz)//(fac(na-1)*fac(nz))
    if cnt<=seq:
        return 'a'+f(na-1, nz,cnt)
    else: 
        return 'z'+ f(na,nz-1,cnt-seq)
if fac(n+m)//(fac(n)*fac(m))<k: print('-1')
else: print(f(n,m,k))

