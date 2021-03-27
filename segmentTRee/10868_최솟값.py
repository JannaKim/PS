import sys; input= lambda: sys.stdin.readline().rstrip()
from math import log
sys.setrecursionlimit(100000)
n, m= map(int, input().split())
floor= int(log(n,2))
if 2**floor<n:
    floor+=1
ground=2**floor
start=ground
seg= [1e9]*2**(floor+1)

for i in range(ground, ground+n):
    seg[i]=int(input())

def heapify(k):
    if k>=ground:
        return seg[k]
    seg[k]=min(heapify(2*k),heapify(2*k+1))
    return seg[k]

heapify(1)
def find(lo, hi, left,right):
    if lo==left and hi==right:
        return seg[(left//2**int(log(right-left+1,2)))]
    if left==right:
        return seg[left]
    mid= (lo+hi)//2
    if right<=mid:
        return find(lo,mid,left,right)
    elif mid+1<=left:
        return find(mid+1,hi,left,right)
    else:
        return min(find(lo,mid,left,mid),find(mid+1,hi,mid+1,right))

for _ in range(m):
    a, b=map(int, input().split())
    a-=1
    b-=1
    print(find(ground, 2*ground-1,ground+a,ground+b))