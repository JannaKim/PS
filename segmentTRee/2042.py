from math import log
n, m, k= map(int, input().split())

tmp= int(log(n,2))

if 2**tmp!=n:
    tmp+=1

sz= 2**tmp
seg= [0]*2**(tmp+1)

for i in range(n):
    inp=int(input())
    seg[sz+i]=inp

def heapify_up(cur):
    if cur>=sz:
        return seg[cur]
    seg[cur]= heapify_up(2*cur)+heapify_up(2*cur+1)
    return seg[cur]

heapify_up(1)

#print(seg)

def update(k,minus):
    if k==0:
        return
    seg[k]-=minus
    update(k//2,minus)


def find(node, lo, hi, st, ed):
    if st>ed or ed < lo or st > hi:
        return 0
    elif st==ed or (lo <= st and hi >= ed):
        return seg[node]
    print(node, lo, hi, st, ed)
    mid= (st+ed)//2
    a= find(node * 2, lo, hi, st,mid)
    b= find(node * 2 + 1, lo, hi, mid+1, ed)
    return a+b
    

for _ in range(m+k):
    a, b, c= map(int, input().split())
    b -= 1
    if a==1:
        delta= seg[sz + b]-c
        update(sz + b, delta)
    elif a==2:
        print(find(1, b, c - 1, 0, n - 1))

'''
if st<lo or ed<hi:
    print(f'{st}<{lo} or {ed}<{hi}')
    return (0,1e9)
'''

'''
10 4
75
30
100
38
50
51
52
20
81
5
'''