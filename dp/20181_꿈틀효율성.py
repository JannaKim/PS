N, K = map(int, input().split())
L = [0]+ [int(i) for i in input().split()]
dp=[0]*(N+1)
for i in range(N,0,-1):
    if L[i]>1:
        s=0
        J=0
        for j in range(i-1,0,-1):
            s+=L[j]
            if s>=K:
                dp[j+1]=max(s-L[j]+L[i]+(dp[i+1] if i+1<=N else 0), (dp[j+2] if j+2<=N else 0))
                J=j+1
                break
        dp[J] = max(dp[J], (dp[J+1] if J+1<=N else 0))
    if i<N:
        dp[i] = max(dp[i], dp[i+1])
print(dp[1])

'''
9 6
1 5 4 4 2 3 10 3 5
'''