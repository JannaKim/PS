N, C = [int(i) for i in input().split()]
L=[]
for i in range(N):
    L.append(int(input()))

L.sort()


def chop(low,high):
    m = (low+high)//2
    if low==high:
        return print(low)
    cnt = C
    here=1
    now=0
    y=0
    #elif L[here]-L[now]>m: #기준집~here집 거리가 m이상이다: m 줄여야함
    #    return chop(low,m)
    while(0<cnt-1): # 공유기 C개 설치 1/ 2 4/ 8/ 9
        while L[here]-L[now]<m: # h=3 돼서 9-8<2
            y=1  # 기준집~here집 거리가 m이하면 here집에는 공유기 설치 못함
            if here<N-1: here+=1 # here집 커서 한칸 더 옮김
            else:break
            
        if(y==1): # L[here]-L[now]<m 실행됐을때만
            y=0
            if here<N-1: #4
                cnt-=1 
                now=here # 기준집~here집 거리가 m이상이므로 공유기 설치
            
            else: return chop(low,m) # 공유기 다 설치 못했다 = m 너무 크다
        else: #기준집~here집 거리가 m이상이다 = m 줄여야한다.
            return chop(low,m)
    return chop(m+1,high) #공유기 다 설치 됐다 = m값 키워도 되겠따.






chop(1,1e9) # 이진캄색 의 m이 정답이면 문제가 풀릴까?