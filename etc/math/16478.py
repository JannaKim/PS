from math import sqrt
c, b, d= map(int, input().split())
ans=(int(sqrt(c**2-d**2)*sqrt(c**2-b**2)+0.5)-b*d)/c
if ans<0:
    print(-1)
else:
    print(int(ans+0.5))