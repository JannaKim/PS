a, b, c= map(int, input().split())

def mul(a, b):
    if b==0:
        return 1
    if b==1:
        return a%c
    half= mul(a,b//2)
    tmp= half*half
    if b%2:
        return tmp*a%c
    else:
        return tmp%c

print(mul(a, b))