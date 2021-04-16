n, m= map(int, input().split())

def gett(n, m):
    res = 0
    while n > 0:
       n = n // m
       res += n
    return res

def get(n):
    return gett(n, 2), gett(n, 5)

a, b = get(n)

c, d = get(n-m)
e, f = get(m)
#print(a,b,c,d,e,f)
#print(min(a,b)-min(e,f)- min(c,d))
print(min(a -c-e, b-d-f))