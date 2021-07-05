n = int(input())
m = int(input())
par = list(range(n + 1))

def find(v):
    if par[v] == v:
        return v
    par[v] = find(par[v])
    return par[v]
def union(u, v):
    r1 = find(u)
    r2 = find(v)
    if r2 < r1:
        r1, r2 = r2, r1
    par[r2] = r1

for _ in range(m):
    a, b = map(int, input().split())
    union(a, b)

ans = 0
for i in range(2, n + 1):
    find(i)
    if par[i] == 1:
        ans += 1
print(ans)