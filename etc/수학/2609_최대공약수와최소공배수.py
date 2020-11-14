A, B = map(int,input().split())
def gcd(a,b):
    if a==0 or b==0:
        return a+b
    elif a>b:
        return gcd(a%b, b)
    else:
        return gcd(a,b%a)

def lcm(a,b):
    i = max(a,b) +1
    while i%a or i%b:
        i+=1
    print(i%a, i%b)
    return i

        
print(gcd(A,B))
print(lcm(A,B))