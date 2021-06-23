n = int(input())
L = [*map(int, input().split())]
top = -1
for i in range(1,n):
    if L[i-1] >= L[i]:
        top = i
        break
if top < 0:
    print('YES')
else:
    curve = -1
    for i in range(top,n):
        if L[i-1] <= L[i]:
            curve = i
            break
    if curve < 0:
        print('YES')
    else:
        print('NO')
