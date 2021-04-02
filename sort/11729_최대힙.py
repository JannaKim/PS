import sys; input= lambda: sys.stdin.readline().rstrip()
from math import log
stc=[0]
top=0
n= int(input())

def heapify(k):
    if k>=2**int(log(top+1,2)):
        return
    left= 2*k
    right= 2*k+1
    if left>top:
        return
    elif right>top:
        if stc[left]>stc[k]:
            stc[left], stc[k]= stc[k],stc[left]
            heapify(left)
    else:
        if stc[left]>stc[right] and stc[left]>stc[k]:
                stc[left], stc[k]= stc[k],stc[left]
                heapify(left)
        else:
            if stc[right]>stc[k]:
                stc[right], stc[k]= stc[k],stc[right]
                heapify(right)


def heapify_up(k):
    if k==1:
        return
    half= k//2
    if stc[k]>stc[half]:
        stc[half], stc[k]= stc[k],stc[half]
        heapify_up(half)
    
for _ in range(n):
    
    ths= int(input())
    if not ths:
        if not top:
            print(0)
        else:
            stc[1], stc[top]= stc[top], stc[1]
            print(stc.pop())
            top-=1
            heapify(1)
            #print(stc)
    else:
        stc.append(ths)
        top+=1
        heapify_up(top)
        #print(stc)