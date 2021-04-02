import sys; input= lambda: sys.stdin.readline().rstrip()
from math import log
sys.setrecursionlimit(50000)
while True:
    L= [*map(int, input().split())]
    if not L[0]:
        break
    # start, ground 필요
    floor= int(log(L[0],2))
    if 2**floor<L[0]:
        floor+=1
    start=2**floor
    ground=start

    seg= [0 for _ in range(2**(floor+1))]
    for idx, i in enumerate(range(start,start+L[0])):
        seg[i]=idx+1

    def heapify(k):
        if k>=start:
            return seg[k]
        left= heapify(2*k)
        right= heapify(2*k+1)
        if L[left]<=L[right]:
            seg[k]=left
        else:
            seg[k]=right
        return seg[k]
    heapify(1)



    def query(node, lo, hi, st, ed):
        #print('query', node, lo, hi, st, ed)
        
        if st>ed or ed < lo or st > hi:
            #print(node, lo, hi, st, ed)
            return -1
        elif st==ed or (lo <= st and hi >= ed):
            #print(f'{st}=={ed} or ({lo} <= {st} and {hi} >= {ed})')
            #print('found',node)
            return node
        
        mid= (st+ed)//2
        #print('mid', mid)
        a= query(node * 2, lo, hi, st, mid)
        b= query(node * 2 + 1, lo, hi, mid+1, ed)
        #print('a, b', a, b)
        if a<0:
            return b
        elif b<0:
            return a
        #if a>L[0]:

        if L[seg[a]]<=L[seg[b]]:
            return a
        else:
            return b
            


    def measure(lo, hi):
        #print('try',lo, hi)
        if lo<1 or hi>L[0]:
            return 0
        if lo == hi:
            return L[lo]
        if lo>hi:
            return 0
    
        least= query(1, lo, hi, 1, ground)
        least=seg[least]
        #print('lesast',least)
        #print(lo, hi, 's least',least)
        tmp= max([ (hi-lo+1)*L[least], measure(lo, least-1), measure(least+1, hi)])

        return tmp
    #print(ground)
    print(measure(1,L[0]))
    #print(seg)

    #print(query(1, 2, 4, 1, L[0]))





    '''
    7 2 1 4 5 1 3 3
    ans= 8

    6 1 2 3 4 5 1
    ans= 9
    '''