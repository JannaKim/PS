def gcd(a, b):
    if a*b==0:
        return a+b
    if a>b:
        return gcd(a%b, b)
    else:
        return gcd(a,b%a)

for _ in range(int(input())):
    a, b= map(int, input().split())
    print(a*b//gcd(a,b))