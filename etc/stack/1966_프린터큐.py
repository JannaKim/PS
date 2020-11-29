from collections import deque

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    L=[int(i) for i in input().split()]
    doc  = M
    Q = deque()
    for idx, el in enumerate(L):
        if idx==doc:
            Q.append((el,True))
        else:
            Q.append((el,False))
    cnt=0
    while True:
        q = Q.popleft()
        for el in Q: # for문으로 덱 돌 수 있다
            if el[0]>q[0]:
                Q.append(q)
                q=(0,False) # 프린트 되는 요소가 아니므로
                cnt-=1
                break
        # print q

        cnt+=1
        if q[1]:
            print(cnt)
            break
    

'''
3
1 0
5
4 2
1 2 3 4
6 0
1 1 9 1 1 1
'''
