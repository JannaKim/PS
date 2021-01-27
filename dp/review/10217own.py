# dp[i][j]: 1- i min time when cost is j
r= range; I= input
tc= int(I())
while tc:
    tc-=1
    n, m, k= map(int, I().split())
    L= [tuple([*map(int, I().split())]) for _ in r(k)] # a, b, cost, dur
    dp= [[1e7 for _ in r(m+1)] for __ in r(n+1)]
    dp[1][0]= 0
    for i in r(m+1):
        for a, b, c, d in L:
            if i-c>=0:
                dp[b][i]= min(dp[b][i], dp[a][i-c]+d)
    ans= min(dp[n])
    print([ans, 'Poor KCM'][ans==1e7])
