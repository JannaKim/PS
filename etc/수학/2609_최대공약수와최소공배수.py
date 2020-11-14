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
    return i

        
print(gcd(A,B))
print(lcm(A,B))

'''
둘 다 나눠 떨어지려면 i%a or i%b를 해줘야 
0 or 0일 경우 while문이 break된다.
'''