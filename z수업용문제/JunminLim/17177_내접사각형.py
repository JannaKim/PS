from math import sqrt
a,b,c=map(int,input().split())
d=(int(sqrt((a**2-b**2)*(a**2-c**2))+0.5)-(b*c))/a
if d<=0:
    print(-1)
else:
    print(int(d+0.5))