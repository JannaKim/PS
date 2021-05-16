a= int(input())
L=[]
for t in range(0,a+a-1):
    L.append([' ']*(a+a-1))
for i in range(0,a+a-1):
    for g in range(0,a+a-1):
        for r in range(0,a):
            if abs(i-(a-1))+abs(g-(a-1))==r:
                L[i][g]='*'


y, x= 0, 2*a-1

for i in range(0,a+a-1):
    for g in range(0,a+a-1):
        for r in range(0,a):
            if abs(i-y)+abs(g-x)<=a-1:
                L[i][g]=''




y, x= 2*a-1, 2*a-1

for i in range(0,a+a-1):
    for g in range(0,a+a-1):
        for r in range(0,a):
            if abs(i-y)+abs(g-x)<=a:
                L[i][g]=''

for i in range(0,a+a-1):
    print(''.join(L[i]))