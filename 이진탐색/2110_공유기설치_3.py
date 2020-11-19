# 8:50 ~ 8:59
N, C = map(int, input().split())
L = [int(input()) for _ in range(N)]
L.sort() #

def install(R):
    lastly_installed=0 # idx
    cnt=C-1
    while cnt:
        if lastly_installed+1>N-1: # for문 안에서만 while 반복 변수를 내려주는 구문을 만들때
            # for문에 아예 들어가지 않을 경우를 생각해줘야 한다
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
print(BS(1,int(1e9)))
