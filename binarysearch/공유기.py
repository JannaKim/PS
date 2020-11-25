N, C = [int(i) for i in input().split()]
L = []
for i in range(N):
    L.append(int(input()))

L.sort()

two_left=False
def chop(low, high):
    global two_left
    #print(low,high)
    m = (low+high)//2
    if low>=high: # 경우의 수가 하나 남았을 때
        return low
    if high-low==1: # 경우의 수 두개 남았을 때
        two_left=True
        m = high
    cnt = C-1
    here = 1
    now = 0
   
    while cnt:  # 공유기 C개 설치 1/ 2 4/ 8/ 9
        if here>=N:#설치할 공유기가 남았는데 못함: 최대 거리 줄이기
            if two_left:
                return low
            else:
                return chop(low, m-1)
        while L[here]-L[now] < m:  # h=3 돼서 9-8<2
            # 기준집~here집 거리가 m이하면 here집에는 공유기 설치 못함
            if here < N-1:
                here += 1  # here집 커서 한칸 더 옮김
            else: # 보는 집이 마지막 집:
                #설치할 공유기가 남았는데 못함: 최대 거리 줄이기
                if two_left:
                    return low
                else:
                    return chop(low, m-1)
        
        # L[here]-L[now]>=m 인 here을 찾았다
        cnt -= 1
        now = here  # 설치된 마지막 공유기에 해당하는 인덱스로 now바꿈
        here = now+1
    if two_left:
        return high
    else:
        return chop(m, high)  # 공유기 다 설치 됐다 = m값 키워도 되겠따.



print(chop(1, int(1e9)))  # 이진캄색 의 m이 정답이면 문제가 풀릴까?