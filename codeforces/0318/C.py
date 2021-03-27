#no more than 𝑛−1 direction changes.

import sys; input= lambda: sys.stdin.readline().rstrip()
for _ in range(int(input())):
    n= int(input())
    L=[*map(int, input().split())]
    odd=[1e9,-1]
    for i in range(1,n,2):
        if L[i]<odd[0]:
            odd=[L[i],i]
    even=[1e9,-1]
    for i in range(0,n,2):
        if L[i]<even[0]:
            even=[L[i],i]

    end= max(odd[1], even[1])
    
    gap= abs(odd[1]- even[1])
    lo, hi= odd[1],even[1]
    if lo>hi:
        lo, hi= hi, lo
    ans=0
    walks=2*n
    prv=0
    for i in range(end+1):
        print('remains',walks)
        if i==lo:
            tmp=n-prv//2-gap//2
            walks-=tmp
            ans+=tmp*L[i]
            prv+=tmp
            print(ans)
            continue
        if i==end:
            ans+=L[i]*walks
            print(ans)
            break
        walks-=1
        prv+=1
        ans+=L[i]
        print(ans)
    print(ans)




'''
5
5
10 1 10 10 1
'''