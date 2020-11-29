N, K = map(int, input().split())
w, v= [0]*N, [0]*N
for i in range(N):
    w[i], v[i] = map(int, input().split())

dp=[0]*(K+1)

for good in range(N):
    for i in range(K,-1,-1):
        if dp[i] or i==0:
            if i+w[good]<=K:
                dp[i+w[good]] = max(dp[i+w[good]], dp[i]+v[good])
print(max(dp))

'''
4 7
6 13
4 8
3 6
5 12
'''
