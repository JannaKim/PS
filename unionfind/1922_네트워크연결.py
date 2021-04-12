import sys; input= lambda: sys.stdin.readline().rstrip()
from heapq import heappop, heappush
n= int(input())
m= int(input())
q=[]
for _ in range(m):
    a, b, c= map(int, input().split())
    heappush(q, (c, a, b))

ln= n-1

def find(v):
    if p[v]!=v:
        p[v]= find(p[v])
        return p[v]
    else:
        return v

def union(u, v):
    r1= find(u)
    r2= find(v)
    p[r1]=r2

p= list(range(n+1))
ans=0
while ln:
    c, a, b= heappop(q)
    #print(c,a,b)
    if find(a)==find(b):
        continue
    union(a,b)
    #print(p)
    ans+=c
    ln-=1
print(ans)