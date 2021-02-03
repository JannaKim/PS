from functools import cmp_to_key as cmp
n= int(input())
L=[]
for _ in range(n):
    L.append(tuple(map(int, input().split())))
L.sort(key=cmp(lambda a, b:a[0]-b[0] if a[1]==b[1] else a[1]-b[1]))

[print(*el) for el in L]
