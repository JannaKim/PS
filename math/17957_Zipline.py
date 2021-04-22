from math import sqrt
for _ in range(int(input())):
    w, g, h, r= map(int, input().split())
    a= g-r
    b= h-r
    mn=1e9


    def cal(c):
        return sqrt(a**2+c**2)+sqrt(b**2+(w-c)**2)

    lo=0
    hi=w

    while lo<hi:
        #print(lo,hi)
        d= (hi-lo)/3
        left=lo+d
        right=hi-d
        #print(left,right)
        if cal(left)<cal(right):
            hi=right-0.000001
        elif cal(left)>cal(right):
            lo= left+0.000001
        else:
            lo=left+0.000001
            hi=right-0.000001
    one= cal(lo)
    two= cal(hi)
    if one<two:
        print(sqrt(w**2+abs(a-b)**2), one)
    else:
        print(sqrt(w**2+abs(a-b)**2), two)

'''
9 9 5 1


for TEST in range(int(input())):
    w, h1, h2, r = map(int,input().split())
    h1-= r; h2-= r
    mind = (abs(h1-h2)**2 + w**2)**.5
    maxd = ((h1+h2)**2 + w**2)**.5
    print(mind, maxd)
'''