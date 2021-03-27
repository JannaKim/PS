from heapq import heappush, heappop
from bisect import bisect_left as bs
# 비싼걸 작은 가방부터
n, k= map(int, input().split())
jew= []
for _ in range(n):
    w, v= map(int, input().split())
    heappush(jew, (-v,w)) # 가방에 들어가는 보석만 힙큐에 넣음

bag= [int(input()) for _ in range(k)]
bag.sort()
chk= [False]*k


for el in bag:

