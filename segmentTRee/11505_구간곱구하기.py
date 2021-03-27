import sys; input= lambda: sys.stdin.readline().rstrip()
from math import log
M= int(1e9)+7
n, m, k= map(int, input().split())
floor= int(log(n,2))
if 2**floor<n:
    floor+=1
ground=2**floor
start=ground
seg=[1]*2**(floor+1)

for i in range(start,start+n):
    seg[i]=int(input())

def heapify(k):
    if k>=ground:
        return seg[k]
    seg[k]= heapify(k*2)*heapify(k*2+1)%M
    return seg[k]
heapify(1)
def update(k):
    if not k:
        return
    seg[k]=seg[k*2]*seg[k*2+1]%M
    update(k//2)

def find(lo, hi, left, right):
    #print(lo, hi, left, right)
    if lo==left and hi==right:
        return seg[left//2**int(log(right-left+1,2))]
    mid= (lo+hi)//2
    if left==right:
        return seg[left]
    if right<=mid:
        return find(lo,mid,left,right)%M
    elif mid+1<=left:
        return find(mid+1,hi,left,right)%M
    else:
        return find(lo,mid,left,mid)*find(mid+1,hi,mid+1,right)%M

for _ in range(m+k):
    a, b, c= map(int, input().split())
    if a==1:
        seg[start+b-1]=c
        update((start+b-1)//2)
        #print(seg)
    elif a==2:
        print(find(start,start+ground-1,start+b-1,start+c-1))
