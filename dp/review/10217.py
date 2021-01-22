r= range
tc= int(input())
while tc:
    tc-=1
    n, m, k= map(int, input().split())
    L= [tuple([*map(int, input().split())]) for _ in r(k)] # a, b, cost, dur

    dp= [[1e7 for _ in r(m+1)] for __ in r(n+1)]
    dp[n][0]= 0
    for i in r(m+1):
        for a, b, cost, dur in L:
            if i-cost>=0:
                dp[a][i]= min(dp[a][i], dp[b][i-cost]+dur)
    ans= min(dp[1])
    print([ans, 'Poor KCM'][ans==1e7])