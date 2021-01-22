# dp[i][j]: 1- i min time when cost is j
r= range
tc= int(input())
while tc:
    tc-=1
    n, m, k= map(int, input().split())
    L= [tuple([*map(int, input().split())]) for _ in r(k)] # a, b, cost, dur

    dp= [[1e7 for _ in r(m+1)] for __ in r(n+1)]
    dp[1][0]= 0
    for i in r(m+1):
        for a, b, cost, dur in L:
            if i-cost>=0:
                dp[b][i]= min(dp[b][i], dp[a][i-cost]+dur)
    ans= min(dp[n])
    print([ans, 'Poor KCM'][ans==1e7])
