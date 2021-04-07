import sys; input= lambda: sys.stdin.readline().rstrip()
from itertools import permutations as per
n, m= map(int, input().split())
L=[*map(int, input().split())]
L.sort()


for el in per(L,m):
    print(*list(el))

