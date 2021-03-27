from math import log
n, m= map(int, input().split())

tmp= int(log(n,2))

if 2**tmp!=n:
    tmp+=1

sz= 2**tmp
seg= [[0,1e9]]*2**(tmp+1)

for i in range(n):
    inp=int(input())
    seg[sz+i]=(inp, inp)

def heapify_up(cur):
    if cur>=sz:
        return seg[cur]
    seg[cur]= (max(heapify_up(2*cur)[0],heapify_up(2*cur+1)[0]), min(heapify_up(2*cur)[1],heapify_up(2*cur+1)[1]))
    return seg[cur]

heapify_up(1)

#print(seg)

def find(node, lo, hi, st, ed):
    if st>ed:
        return (0,1e9)
    elif st==ed or (lo <= st and hi >= ed):
        print(node, lo, hi, st, ed)
        return seg[node]
    
    mid= (st+ed)//2
    a, b= find(node * 2, lo, hi, max(st,lo),mid)
    c, d= find(node * 2 + 1, lo, hi, mid+1, min(ed,hi))
    return (max(a,c), min(b,d))
    

for _ in range(m):
    a, b= map(int, input().split())
    print(*find(1, a - 1, b - 1, 0, n - 1)[::-1])

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