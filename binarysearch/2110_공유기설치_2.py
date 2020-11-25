N, C =map(int,input().split())

L = [int(input()) for _ in range(N)]
L.sort()

def install(R): # 가장 인접한 두 공유기 사이 최대 거리
    # 일단 맨 앞집에 하나 설치
    last_installed = 0

    cnt=C-1 # 설치해야할 공유기 개수
       
    while cnt:
        if last_installed+1>=N: # 마지막 집에 설치를 했는데,
            # 설치할 공유기가 더 남았을때 False 돌려줘야 한다
            return False
        for i in range(last_installed+1,N): # 2<= N <= 200000
            if L[i]-L[last_installed]>=R:              
                cnt-=1
                last_installed= i # i번째 집에 설치했다
                break # 다음 공유기 설치하기
            if i==N-1 and cnt!=0: # 마지막 집까지 갔지만 설치 다 못함
                return False           
    return True

def BS(a, b):
    if b<=a:
        return a
    elif b-a==1:
        if install(b):
            return b
        else:
            return a
    else:
        m = (a+b)//2
        if install(m): # 설치가 되면
            return BS(m,b) # 더 큰 거리로 설치 할 수 있나 봐야함
        else:
            return BS(a,m-1)

print(BS(1,int(1e9)))




   

