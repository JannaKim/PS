#11:26 12:23
import sys; input=lambda: sys.stdin.readline().rstrip()
N, C = map(int, input().split())
L = [int(input()) for _ in range(N)]
L.sort()
def install(R):
    lastly_installed=0
    cnt = C-2
    while cnt:
        if lastly_installed+1>=N-1:
            return False
        for i in range(lastly_installed+1,N-1):
            if L[i]-L[lastly_installed]>=R:
                cnt-=1
                lastly_installed=i
                break
            if i==N-2 and cnt!=0:
                # 가능한 모든집 확인했는데 공유기 설치 다 못함
                return False
    if L[-1]-L[lastly_installed]>=R:
        return True
    else:
        return False

def BS(a,b):
    if a>=b:
        return a
    elif b-a==1:
        if install(b):
            return b
        elif install(a):
            return a
        else:
            return -1

    else:
        m = (a+b)//2
        if install(m):
            return BS(m,b)
        else:
            return BS(a,m-1)
if C==2:
    print(L[-1]-L[0])
elif N==2:
    print(-1)
else:
    print(BS(1,int(1e9)))