import sys; input= lambda: sys.stdin.readline().rstrip()
from heapq import heappop, heappush
n= int(input())
mx=-1
lec= [False]*10001
q=[]
for _ in range(n):
    a, b= map(int, input().split())
    heappush(q,(-a,b))
ans=0
while q:
    p, d= heappop(q)
    p=-p
    for i in range(d,0,-1):
        if not lec[i]:
            #print(i, p)
            ans+=p
            lec[i]=True
            break
print(ans)
