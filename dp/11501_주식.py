import sys; input= lambda: sys.stdin.readline().rstrip()
from heapq import heappush, heappop
for _ in range(int(input())):
    n= int(input())
    L= [*map(int, input().split())]
    if n==1:
        print(0)
        continue
    H=[]
    for el in L:
        heappush(H,-el)
    profit=0
    amount=0
    i=0
    mx=-heappop(H)
    box=0
    for el in L:
        if el==mx:
            profit+=(el*amount-box)
            amount=0
            box=0
            if H:
                mx=-heappop(H)
        elif el<mx:
            amount+=1
            box+=el
            
    print(profit)
'''
1
6
1 9 1 9 2 8


1
6
1 1 3 1 1 0

1
6
1 3 2 6 7 8
'''
