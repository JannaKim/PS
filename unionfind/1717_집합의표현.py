import sys; input= lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(1000000)
n, m= map(int, input().split())
parent= list(range(n+1))
def find(v):
    if parent[v]!=v:
        parent[v]=find(parent[v])
        return parent[v]
    else:
        return v

def union(u, v):
    root1= find(u)
    root2= find(v)
    parent[root1]=root2

for _ in range(m):
    q, a, b= map(int, input().split())
    if q==0:
        union(a,b)
    else:
        parent[a]=find(a)
        parent[b]=find(b)
        if parent[a]==parent[b]:
            print('YES')
        else:
            print('NO')