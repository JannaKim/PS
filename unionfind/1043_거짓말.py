import sys; input= lambda: sys.stdin.readline().rstrip()
n, m= map(int, input().split())
tru= [*map(int, input().split())]
par= list(range(1+n))

def find(v):
    if par[v]==v:
        return v
    else:
        par[v]= find(par[v])
        return par[v]

def union(u, v):
    r1= find(u)
    r2= find(v)
    if r1>r2:
        r1, r2= r2, r1
    par[r2]=r1
knows= 0
if tru[0]:
    knows= tru[1]
    for i in range(2,2+tru[0]-1):
        union(tru[i],tru[i-1])
knows=par[knows]
#print(knows)
for i in range(1,n+1):
    find(i)
party= []
for _ in range(m):
    party.append([*map(int, input().split())])
    for a, b in zip(party[-1][1:], party[-1][2:]):
        union(a,b)

for i in range(1,n+1):
    find(i)
knows= par[knows]

ans=0
#print(par,knows)
for j in range(m):
     if par[knows] not in [par[party[j][i]] for i in range(1,1+party[j][0])]:
         ans+=1
print(ans)

'''
6 5
1 6
2 4 5
2 1 2
2 2 3
2 3 4
2 5 6
'''




