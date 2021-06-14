# 7:58 ~ 8:08
from collections import deque
n , m = map(int, input().split())
B = [0] * 101
for _ in range(n + m):
    a , b = map(int, input().split())
    B[a] = b

def bound(k):
    if 1 <= k <=100:
        return True
    return False
def move(loc , dice):
    if B[loc + dice]:
        return B[loc + dice]
    else:
        return loc + dice
def BFS():
    q = deque()
    q.append((1,0))
    chk = [False] * 101
    chk[1] = True
    while q:
        loc , step = q.popleft()
        if loc == 100:
            return step
        for i in range(1, 1 + 6):
            if not bound(loc + i):
                continue
            cur = move(loc , i)
            if not chk[cur]:
                chk[cur] = True
                q.append( (cur, step + 1))

print(BFS())