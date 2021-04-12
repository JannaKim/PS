import sys; input= lambda: sys.stdin.readline().rstrip()
from heapq import heappop, heappush

v, e= map(int, input().split())
q=[]
for _ in range(e):
    a, b, c= map(int, input().split())
    heappush(q, (c,a,b))

ln=v-1
ans=0
p= list(range(v+1))
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

while ln:
    c, a, b= heappop(q)
    if find(a)==find(b):
        continue
    union(a,b)
    ln-=1
    ans+=c

print(ans)