import sys; input= lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(100000)
n, m, k= map(int, input().split())
mp=[list(input()) for _ in range(n)]
DY=[0,0,1,1,1,-1,-1,-1]
DX=[1,-1,0,1,-1,0,1,-1]
dic={}
def rec(y, x, idx,s):
    if s not in dic:
        dic[s]=0
    dic[s]+=1
    if idx==6:
        return
    for dy, dx in zip(DY, DX):
        ny=(y+dy+n)%n
        nx=(x+dx+m)%m
        rec(ny, nx, idx+1,s+mp[ny][nx])
L=[]
for _ in range(k):
    tmp=input()
    L.append(tmp)
    dic[tmp]=0

for i in range(n):
    for j in range(m):
        rec(i, j, 1,mp[i][j])
for el in L:
    print(dic[el])

'''
n, m, Q = map(int,input().split())
grid = [input() for i in range(n)]

for QUERY in range(Q):
    s = input()
    dp = [[int(c == s[0]) for c in row] for row in grid]
    for nch in s[1:]:
        ndp = [[0]*m for i in range(n)]
        for i in range(n):
            for j in range(m):
                for ni,nj in (i-1,j-1),(i-1,j),(i-1,j+1),(i,j-1),(i,j+1),(i+1,j-1),(i+1,j),(i+1,j+1):
                    ni%= n; nj%= m
                    if grid[ni][nj] != nch: continue
                    ndp[ni][nj]+= dp[i][j]
        dp = ndp
    print(sum(map(sum, dp)))
'''