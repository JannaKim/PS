import sys; input= lambda: sys.stdin.readline().rstrip()
from math import log

n, m, k= map(int, input().split())

floor= int(log(n,2)) # floor: 바닥길이
start= 2**floor
if start<n:
    floor+=1
start= 2**floor
ground= 2**floor
seg= [0]* 2**(floor+1)

def heapify(k):
    if k>=start:
        return seg[k]
    seg[k]=heapify(2*k)+heapify(2*k+1)
    return seg[k]

for i in range(start,start+n):
    seg[i]=int(input())
heapify(1)

def change(ths, gap):
    if not ths:
        return 
    seg[ths]+=gap
    change(ths//2,gap)

def add(lo, hi, a, b):
    if lo==a and hi==b:
        return seg[a//2**int(log(b-a+1,2))] # 격자 맞으면 바로 보냄
    if a>b:
        return 0
    mid= (lo+hi)//2
    
    return add(lo, mid, max(lo,a),min(b,mid))+ add(mid+1, hi,max(a,mid+1),min(b,hi))

for _ in range(m+k):
    a, b, c= map(int, input().split())
    if a==1:
        delta= c- seg[start+b-1]
        change(start+b-1,delta)
    elif a==2:
        print(add(start,start+ground-1,start+b-1, start+c-1))