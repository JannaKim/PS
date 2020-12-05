from functools import cmp_to_key as cmp
from sys import*; input= lambda: stdin.readline().rstrip()

N = int(input())
L = []
for i in range(N):
    a, b = input().split()
    L.append((int(a),b,i))

L.sort(key = cmp(lambda a, b: a[2]-b[2] if a[0]==b[0] else a[0]-b[0]))

[print(*el[:2]) for el in L]