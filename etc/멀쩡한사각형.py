'''
W, H = map(int,input().split())
def gcd(a,b):
    if a==0 or b==0:
        return a
    if a>b:
        return gcd(b,a%b)
    if b>a:
        return gcd(a,b%a)

w = W//gcd(W,H)
h = H//gcd(W,H)

def sol(W,H, w, h):
    return W*H - gcd(W,H)*solution(w,h)

def solution(w,h):
    return w+h-1

print(sol(W,H,w,h))


'''
def solution(w,h):
    def gcd(a,b):
        if a==0 or b==0:
            return a+b
        if a>=b:
            return gcd(b,a%b)
        if b>a:
            return gcd(a,b%a)
    GCD = gcd(w,h)
    _w = w//GCD
    _h = h//GCD
    
    answer = w*h- GCD*(_w+_h-1)
    return answer

print(solution(1,1))

'''
def gcd(a,b): return b if (a==0) else gcd(b%a,a)    
def solution(w,h): return w*h-w-h+gcd(w,h)
'''
