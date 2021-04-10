x, y, c= map(float, input().split())


lo=0.0001
hi= min(x, y)-0.0001

ans=0

def f(k):
    h1= (x**2-k**2)**0.5
    h2= (y**2-k**2)**0.5
    #print((h1*h2)/(h1+h2))
    return (h1*h2)/(h1+h2)


while hi-lo>0.0001:
    m= (lo+hi)/2
    #print(lo, hi)
    if f(m)>=c:
        ans=m
        lo=m
    else: # c 작으면 길이줄이기
        hi=m-0.0001
print(ans)