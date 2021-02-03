n, m= map(int, input().split())
L= [*map(int, input().split())]
def cut(saw):
    return sum([max(el-saw,0) for el in L ])
    
lo= 0
hi= int(1e9)
while lo<hi-1:
    mid= (lo+hi)//2
    if cut(mid)<m:
        hi= mid-1
    else:
        lo=mid # mid: lo
print([lo, hi][cut(hi)>=m])
