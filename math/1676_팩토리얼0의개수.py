n= int(input())
s=0
if n>=125:
    s+=n//125
if n>=25:
    s+=n//25
if n>=5:
    s+=n//5
print(s)