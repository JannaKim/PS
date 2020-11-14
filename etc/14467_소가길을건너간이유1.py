cow = []
[cow.append([]) for _ in range(10)]

N = int(input())

for _ in range(N):
    a, b = [int(i) for i in input().split()]
    cow[a-1].append(str(b))

cnt=0
for cross in cow:
    if cross:
        now = cross[0]
        for road in cross:
            if now==road:
                pass
            else:
                cnt+=1
                now=road

print(cnt)
'''
8
3 1
3 0
6 0
2 1
4 1
3 0
4 0
3 1
'''