import sys; input= lambda: sys.stdin.readline().rstrip()
from collections import deque
seg= deque()
seg.append(0)
top=0
n= int(input())
def heapify_up(k):
    if k==1:
        return
    half=k//2
    if seg[k]<seg[half]:
        seg[k], seg[half]= seg[half], seg[k]
        heapify_up(half)

def heapify(k):
    global top
    here=0
    left=k*2
    right=k*2+1
    if left>top:
        return
    elif right>top:
        here=left
    else:
        if seg[left]>seg[right]:
            here= right
        else:
            here=left
    if seg[k]>seg[here]:
        seg[k], seg[here]= seg[here], seg[k]
        heapify(here)


for _ in range(n):
    inp= int(input())
    if inp==0:
        if top==0:
            print(0)
        else:
            print(seg[1])
            seg[1], seg[top]= seg[top], seg[1]
            seg.pop()
            top-=1
            if top>0:
                heapify(1)
            #[print(el,end=' ') for el in seg]
            #print()
    else:
        seg.append(inp)
        top+=1
        heapify_up(top)
        #[print(el,end=' ') for el in seg]
        #print()


