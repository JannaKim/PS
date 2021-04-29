
def solution(n, cards):
    dp= [0]+[1e9]*n
    for c in cards:
        for i in range(n+1):
            if (i==0 or dp[i]) and i+c<=n:
                dp[i+c]= min(dp[i+c], dp[i]+1)
    return dp[n]
    
print(solution(8, [1,2,6,8]))