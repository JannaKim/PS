L=[int(input()) for _ in range(28)]
L.sort()
lo= 1
hi= 28
while hi-lo>=1:
    m= (hi+lo)//2
    if L[m]==m:
        