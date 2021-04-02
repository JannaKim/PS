import sys; input= lambda: sys.stdin.readline().rstrip()
'''
n= int(input())
top=0
seg=[0]

def heapify_up(k):
    if k==1:
        return
    half=k//2
    if seg[half]>seg[k]:
        seg[half], seg[k]= seg[k], seg[half]
        heapify_up(half)

def heapify(k):
    child=0
    left=2*k
    right=2*k+1
    if left>top:
        return
    elif right>top:
        child=2*k
    else:
        if seg[left]<seg[right]:
            child=left
        else:
            child=right
    seg[child], seg[k]= seg[k], seg[child]
    heapify(child)

for _ in range(n):
    seg.append(int(input()))
    top+=1
    heapify_up(top)


for i in range(1,n+1):
    seg[1], seg[top]= seg[top], seg[1]
    print(seg.pop())
    top-=1
    heapify(1)

# 1억: 381MB
# 천: 38MB
'''

ls= [0]*10001
n= int(input())
for _ in range(n):
    ls[int(input())]+=1

for i in range(1,10001):
    if ls[i]:
        print((str(i)+'\n')*ls[i],end='')
