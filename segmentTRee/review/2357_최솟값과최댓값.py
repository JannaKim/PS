import sys; input= lambda: sys.stdin.readline().rstrip()
from math import log

n, m= map(int, input().split())
story=int(log(n,2))
if 2**story<n:
    story+=1
ground= 2**story
start= ground
seg= [[1e9,0]]*2**(story+1)
for i in range(start, start+n):
    tmp= int(input())
    seg[i]=[tmp, tmp]

def heapify(k):
    if k>=start:
        return seg[k]
    left= heapify(2*k)
    right=heapify(2*k+1)
    mn= min(left[0],right[0])
    mx= max(left[1],right[1])
    seg[k]= [mn, mx]
    return seg[k]

heapify(1)
def gather(lo, hi, a, b):
    if lo==a and hi==b:
        return seg[a//2**int(log(b-a+1,2))]
    elif a>b:
        return [1e9,0]

    mid= (lo+hi)//2
    if b<=mid:
        return gather(lo,mid,a,b)
    elif mid+1<=a:
        return gather(mid+1,hi,a,b)
    else:
        left=gather(lo,mid,a,mid)
        right=gather(mid+1,hi,mid+1,b)
        mn= min(left[0], right[0])
        mx= max(left[1], right[1])

    return [mn,mx]
for _ in range(m):
    a, b= map(int, input().split())
    print(*gather(start, start+ground-1,start+a-1,start+b-1))