from math import sqrt as root

a,b=map(int, input().split())

m=[-a+root(a**2-b),-a-root(a**2-b)]
if m[0]==m[1]:
    print(int(m[0]))
else:
    print(int(sorted(m)[0]),int(sorted(m)[1]))