def solution(w,h):
    def gcd(a,b):
        if a==0 or b==0:
            return a+b
        if a>=b:
            return gcd(b,a%b)
        if b>a:
            return gcd(a,b%a)
    GCD = gcd(w,h)
    y= w//GCD
    x = h//GCD
    
    answer = w*h- GCD*(x+y-1)
    return answer