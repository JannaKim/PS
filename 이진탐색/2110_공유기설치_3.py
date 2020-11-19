# 8:50 ~ 8:59
N, C = map(int, input().split())
L = [int(input()) for _ in range(N)]
L.sort()
def install(R):
    lastly_installed=0 # idx
    cnt=C-1
    while cnt:
        if lastly_installed+1>N-1:
            return False
        for i in range(lastly_installed+1,N):
            if L[i]-L[lastly_installed]>=R:
                cnt-=1
                lastly_installed=i
                break
            if i==N-1 and cnt!=0:
                return False
    return True


def BS(a,b):
    if a==b:
        return a
    elif b-a==1:
        if install(b): return b
        else: return a
    else:
        m = (a+b)//2
        if install(m):
            return BS(m,b)
        else:
            return BS(a,m-1)
print(BS(1,int(1e9)))
