from heapq import heappop, heappush
while True:
    n= int(input())
    mp= [[-1]*(n+1)]
    mp+= [[-1]+[*map(int, input().split())]+[-1] for _ in range(n)]
    mp+= [[-1]*(n+1)]

    dp= [[1e9]*(n+2) for _ in range(n+2)]
    chk= [[False]*(n+2) for _ in range(n+2)]


    q= []
    heappush(q, (mp[n][n], n, n))
    chk[n][n]= True
    dp[n][n]=mp[n][n] ###### 

    while q:
        cost, i, j= q.pop()

        if dp[i][j]<cost:
            continue

        for dy, dx in zip([0, 0, 1, -1], [1, -1, 0, 0]):
            if mp[i+dy][j+dx]==-1: continue
            if cost+ mp[i+dy][j+dx]< dp[i+dy][j+dx]:
                dp[i+dy][j+dx]= cost+ mp[i+dy][j+dx]
                q.append((dp[i+dy][j+dx], i+dy, j+dx))

    print(dp[1][1])