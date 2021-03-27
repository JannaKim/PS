import sys; input= lambda: sys.stdin.readline().rstrip()
from heapq import heappush, heappop
n, c= map(int, input().split())
for _ in range(n):
    x, y, v= map(int, input().split())
    