from collections import deque
for _ in range(int(input())):
    n, m= map(int, input().split())
    L=[*map(int, input().split())]
    D= deque()
    for idx, el in enumerate(L):
        if idx==m:
            D.append((el, True))
        D.append((el, False))
    O= deque()
    for el in sorted(L, reverse= True):
        O.append(el)
    cnt=0
    while D:
        doc, chk= D.popleft()
        if doc==O[0]:
            cnt+=1
            O.popleft()
            if chk==True:
                print(cnt)
                break
        else:
            D.append((doc, chk))