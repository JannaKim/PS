p1, p2, p3, x1, x2, x3= map(int, input().split())


def gcd(a, b):
    if a*b==0:
        return a+b
    if a>b:
        return gcd(a%b, b)
    else:
        return gcd(a, b%a)


x= gcd(p1, p2)
y= gcd(x, p3)

LCM= y*(p1//y)*(p2//y)*(p3//y)

flag= True
for i in range(1, LCM+1):
    if i%p1==x1 and i%p2==x2 and i%p3==x3:
        flag=False
        print(i)
        break
if flag:
    print(-1)
