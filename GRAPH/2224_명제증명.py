n = int(input())
dic = {}
idx = 0
decode = {}
incode = {}

edge = []

for _ in range(n):
    a, b  = input().split(' => ')
    edge.append((a, b))

    if a not in dic:
        dic[a] = True
        incode[a] = idx
        decode[idx] = a
        idx += 1

    if b not in dic:
        dic[b] = True
        incode[b] = idx
        decode[idx] = b
        idx += 1  

dp = [ [1e9] * idx for _ in range(idx) ]


for a, b in edge:
    dp[incode[a]][incode[b]] = 1

for i in range(idx):
    for j in range(idx):
        for k in range(idx):
            dp[j][k] = min(dp[j][k], dp[j][i] + dp[i][k])


ans = []
for i in range(idx):
    for j in range(idx):
        if i == j:
            continue
        if dp[i][j] != 1e9:
            ans.append((ord(decode[i]), ord(decode[j]), i, j))

ans.sort()
print(len(ans))
for a, b, i, j in ans:
    print(f'{decode[i]} => {decode[j]}' )

'''
par = list(range(10001))

def find(v):
    if par[v]== v:
        return v
    par[v] = find(par[v])
    return par[v]

def union(u, v):
    r1 = find(u)
    r2 = find(v)
    par[r2] = r1

for _ in range(n):
    a, b  = input().split(' => ')
    if a not in dic:
        dic[a] = True
        incode[a] = idx
        decode[idx] = a
        idx += 1

    if b not in dic:
        dic[b] = True
        incode[b] = idx
        decode[idx] = b
        idx += 1

    union(incode[a], incode[b])


for i in range(idx):
    find(i)
print(par)

for i in range(idx):
    find(i)
    if par[i] == i:
        continue
    print(f'{decode[par[i]]} => {decode[i]}')

'''
