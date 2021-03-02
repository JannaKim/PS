from math import log
n, a, b= map(int, input().split())

if b<a:
    a, b= b, a

def match(lo,hi, round):
    if round==1:
        return 1
    global a, b
    m= (lo+hi)//2
    #print(lo, m, m+1, hi)
    if a<=m and b<=m:
        return match(lo, m, round-1)
    elif a>m and b>m:
        return match(m+1, hi, round-1)
    else:
        return round
r= int(log(n,2))
if 2**r<n:
    r+=1
    
print(match(1, 2**r, r))