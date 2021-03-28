import sys; input= lambda: sys.stdin.readline().rstrip()
from math import log
n= int(input())
floor=  int(log(n,2))
if 2**floor<n:
    floor+=1
ground= 2**floor
start= ground

seg= [0]*(2**(floor+1))

L=[*map(int, input().split())]
for idx,i in enumerate(range(start,start+n)):
    seg[i]= L[idx]


def heapify_down(k):
    if k>=ground:
        return seg[k]
    seg[k]= max(heapify_down(2*k), heapify_down(2*k+1))
    return seg[k]

heapify_down(1)
def head_search(k):
    if k>=ground:
        return k
    if seg[2*k+1]== seg[k]:
        return head_search(2*k+1)
    else:
        return head_search(2*k)

ans=0
gap=0
for i in range(start+n-1,start-1,-1):
        if seg[1]==0:
            break
        here=head_search(1)
        ans=ans+i-here+gap
        #print(seg)
        seg[i]=0
        seg[here]=0
        #print(seg)
        heapify_down(1)
        #print(seg)
        #print(ans)
        gap+=1
print(ans)
    


