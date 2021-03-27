n, k= map(int, input().split())
wv=[]
for _ in range(n):
    wv.append(tuple(map(int, input().split())))

dp=[0]*(k+1)
for wei, val in wv:
    for i in range(k,-1,-1):
        if (i==0 or dp[i]) and i+wei<=k:
            dp[i+wei]= max(dp[i+wei], dp[i]+val)  
print(max(dp))      