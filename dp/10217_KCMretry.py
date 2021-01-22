import sys; input= lambda: sys.stdin.readline().rstrip(); r=range
t= int(input())
while t:
    t-=1
    n, m, k= map(int, input().split())
    edge= [[] for _ in r(n+1)]
    while k:
        k-=1
        v, v2, c, d= map(int, input().split())
        edge[v].append((v2, c, d))
    dp=[[int(1e9) for _ in r(m+1)] for __ in r(n+1)]
    dp[1]= [0 for _ in r(m+1)]
    for i in r(m+1):
        for v in r(n,0,-1): 
            if dp[v][i]==int(1e9): continue
            for v2, cost, dur in edge[v]:
                if cost+i<=m:
                    dp[v2][i+cost]= min(dp[v2][i+cost], dp[v][i]+dur)
                    # check if its faster
    ans=dp[n][m]
    print([ans, 'Poor KCM'][ans==int(1e9)])

# heading to its own: dur=0 neglecting the cost 
# if dp[this airport][cur cost]<1e9: there exists a way: can head more

    
