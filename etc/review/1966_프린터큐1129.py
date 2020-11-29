from collections import deque
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    *L,=map(int, input().split())
    Q=deque()
    for idx, el in enumerate(L):
        Q.append((el, (True if idx==M else False)))
    cnt=0
    while True:
        q=Q.popleft()
        PRINTED=True
        for el in Q:
            if el[0]>q[0]:
                PRINTED= not PRINTED # False
                Q.append(q)
                break
        if PRINTED:
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




