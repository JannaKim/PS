while True:
    n= int(input())
    mp= [[-1]*(n+1)]
    mp+= [[-1]+[*map(int, input().split())]+[-1] for _ in range(n)]
    mp+= [[-1]*(n+1)]

    dp= [[1e9]*(n+2) for _ in range(n+2)]
    chk= [[False]*(n+2) for _ in range(n+2)]
    def topdown(i, j):
        if i==1 and j==1:
            return mp[1][1]
        if mp[i][j]==-1:
            return 1e9
        if not chk[i][j]:
            chk[i][j]=True
            dp[i][j]=  mp[i][j]+ min(topdown(i-1, j), topdown(i, j-1), topdown(i+1, j), topdown(i, j+1))
            chk[i][j]=False
            return dp[i][j]
        else:
            return dp[i][j]

    topdown(n, n)
    print(dp[n][n])
    
