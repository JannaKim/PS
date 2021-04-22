from math import sqrt
def gcd(a,b) :
    if a% b == 0 :
        return b
    else :
        return gcd(b,a%b)

r, g= map(int, input().split())
mx= gcd(r,g)

for i in range(1, mx//2+1):
    if not mx%i:
        print(i ,r//i, g//i)
if mx!=1:
    print(mx, r//mx, g//mx)