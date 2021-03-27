# TLE
import sys; input= lambda: sys.stdin.readline().rstrip()
from math import factorial as fac
n= int(input())
L= [*map(int, input().split())]
dp=[0]*n
chk= [False]*(n+1)
def find(i,remain,th):
    if not remain:
        return th
    if i==n:
        return -2
    cur=1
    while True:
        while chk[cur]:
            cur+=1
        if L[i]==cur:
            chk[cur]=True
            return find(i+1,remain-1,th)
        cur+=1
        if not dp[remain-1]:
            dp[remain-1]=fac(remain-1)
        th+=dp[remain-1]

box= [False]*(n+1)   
def create(th, i, remain, q):
    if not remain:
        return q
    if not dp[remain-1]:
        dp[remain-1]=fac(remain-1)
    nxt=dp[remain-1]
    for i in range(1,n+1):
        if not box[i]:
            if th<nxt:
                box[i]=True
                q.append(i)
                return create(th, i+1, remain-1, q)
            th-=nxt


nth=find(0,n,0)
if nth==fac(n)-1:
    print(-1)
else:
    print(*create(nth+1,0,n,[]))
