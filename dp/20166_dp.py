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