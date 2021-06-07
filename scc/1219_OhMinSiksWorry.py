n , st , ed , m = map(int, input().split())
edge = [ [] for _ in range(n)]
cross_edge = [ [] for _ in range(n)]

for _ in range(m):
    a , b , c = map(int, input().split())
    edge[a].append(( b , c))
    cross_edge[b].append(a)
P = [*map(int, input().split())]

chk = [False] * n
stc = []
def dfs(v):
    print(v)
    for v2 in cross_edge[v]:
        if not chk[v2]:
            chk[v2] = True
            dfs(v2)
    stc.append(v)


for i in range(n):
    if not chk[i]:
        chk[i] = True
        dfs(i)
print(stc)
chk = [False] * n
def findscc(v):
    stack = []
    for v2 , c in edge[v]:
        if not chk[v2]:
            chk[v2] = True
            stack += findscc(v2)
    stack.append(v)
    return stack

scc= []
while stc:
    v = stc.pop()
    if not chk[v]:
        chk[v] = True
        tmp = findscc(v)
        if len(tmp) == 1 and v not in edge[v]:
            continue
        scc.append(tmp)
print(scc)
