a, b= map(int, input().split())
def gcd(a, b):
    if not a*b:
        return a+b
    if a>b:
        return gcd(a%b, b)
    else:
        return gcd(a,b%a)
def lcm(a, b, GCD):
    return GCD*(a//GCD)*(b//GCD)

c= gcd(a,b)
print(c, lcm(a,b,c), sep='\n')

'''
a,b = map(int,input().split())

def euc(a,b) :
    if a% b == 0 :
        return b
    else :
        return euc(b,a%b)
        
ans_d = euc(a,b)
ans_m = euc(a,b)*(a/euc(a,b))*(b/euc(a,b))
        
print(ans_d)
print(int(ans_m))
'''
