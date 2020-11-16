A, B = map(int,input().split())
def gcd(a,b):
    if a==0 or b==0:
        return a+b
    elif a>b: # 왜 a>=b하면 런타임에러?
        return gcd(a%b, b)
    else:
        return gcd(a,b%a)

def lcm(a,b):
    i = max(a,b)
    while i%a or i%b:
        i+=1
    return i

        
print(gcd(A,B))
print(lcm(A,B))

'''
둘 다 나눠 떨어지려면 i%a or i%b를 해줘야 
0 or 0일 경우 while문이 break된다.

a,b 의 최대공약수는 a or b일 수 있다!
'''