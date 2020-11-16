N = int(input())
*L, = map(int, input().split())

inc=0
dec=0
#  1 2 3 4 5
for i in range(N-1,-1,-1):
    if L[i-1]<=L[i]:
        continue
    else:
        inc=i
        break

mx1=1

# 1 4 2 3 5
if L[0]>=L[N-1]:
    for i in range(1,inc):
        if L[i-1]<=L[i]:
            continue
        else:
            mx1=-1
            break
else:
    if inc!=0:
        mx1=-1

if mx1>0:
    mx1=inc


for i in range(N-1,-1,-1):
    if L[i-1]>=L[i]:
        continue
    else:
        dec=i
        break

mx2=1
if L[0]<=L[N-1]:
    for i in range(1,dec):
        if L[i-1]>=L[i]:
            continue
        else:
            mx2=-1
            break
else:
    if dec!=0:
        mx2=-1
if mx2>0:
    mx2=dec

if mx1<0 and mx2<0:
    print(-1)
else:
    if mx1<0:
        print(mx2)
    elif mx2<0:
        print(mx1)
    else:
        print(min(mx1,mx2))
