import sys; input= lambda: sys.stdin.readline().rstrip()
from heapq import heappush, heappop
n, k= map(int, input().split())
q= [[0, n]]
sz=int(max(n+1, k+1)*1.5)
chk= [False]*sz
while q:
    t, loc= heappop(q)
    if loc==k:
        print(t)
        exit()
    teleport= loc*2
    if teleport<sz and not chk[teleport]:
        chk[teleport]=True
        heappush(q, (t, teleport))
    if loc+1<sz and not chk[loc+1]:
        chk[loc+1]=True
        heappush(q, (t+1, loc+1))
    if loc-1>=0 and not chk[loc-1]:
        chk[loc-1]=True
        heappush(q, (t+1, loc-1))