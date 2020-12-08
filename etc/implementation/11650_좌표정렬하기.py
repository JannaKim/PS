from functools import cmp_to_key as cmp
N = int(input())
L=[]
for _ in range(N):
    L.append(tuple(map(int, input().split())))

L.sort(key=cmp(lambda a, b: a[1]-b[1] if a[0]==b[0] else a[0]-b[0]))
[print(*el) for el in L]

'''
n,*l=([*map(int,i.split())]for i in open(0));l.sort()
for i in l:print(*i)

https://www.acmicpc.net/source/23043913

import sys
n = int(sys.stdin.readline())
l = []
for _ in range(n):
    l.append([int(i) for i in sys.stdin.readline().split()])
l.sort(key = lambda x : x[0] * 1000000 + x[1])
for i in l:
    print(i[0], i[1])
'''