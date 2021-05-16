from collections import deque
import sys; input= lambda: sys.stdin.readline().rstrip()

def sgn(prv):
    if prv==-1:
        return 1983
    else:
        ths= (prv* 214013 + 2531011)%2**32
        return ths%10000 +1

for _ in range(int(input())):
    k, n= map(int, input().split())
    ans=0
    cur= -1
    s=0
    stc=deque()
    for _ in range(n):
        
        cur= sgn(cur)
        s+=cur
        stc.append(cur)
        print(stc, s)
        while s>k:
            p=stc.popleft()
            s-=p
        print(stc, s)
        if s==k:
            ans+=1
        print(ans)
    print(ans)
