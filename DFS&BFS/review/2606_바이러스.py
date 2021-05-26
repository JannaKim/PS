n= int(input())
parent= list(range(n+1))
m= int(input())

def find(v):
    if parent[v]==v:
        return v
    parent[v]= find(parent[v])
    return parent[v]
def union(u, v):
    r1= find(u)
    r2= find(v)
    parent[r1]=min(r1,r2)
    parent[r2]=min(r1,r2)
for _ in range(m):
    a, b= map(int, input().split())
    union(a,b)
cnt=0
for i in range(2,n+1):
    find(i)
    print(parent)
    if parent[i]==parent[1]:
        cnt+=1
print(cnt)