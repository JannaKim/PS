from functools import cmp_to_key as cmp



N = int(input())

sch=[]
for _ in range(N):
    sch.append(tuple(map(int, input().split())))

sch.sort(key=cmp(lambda a, b: a[0]-b[0] if a[1]==b[1] else a[1]-b[1]))
cnt=1
lastDay=sch[0][1]

for el in sch[1:]:
    if lastDay<=el[0]:
        lastDay=el[1]
        cnt+=1

print(cnt)