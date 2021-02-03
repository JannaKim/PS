n, k= map(int, input().split())
coin=[int(input()) for _ in range(n)]
if k<10000000:
    dp=[0]+[1e9]*k # 1000만 메모리356252KB..? 256mb 넘엇는데?
    for c in coin:
        for i in range(k+1):
            if i+c<=k:
                dp[i+c]= min(dp[i+c], dp[i]+1)
    print(dp[k])
else:
    coin.sort(reverse= True)
    ans=0
    for el in coin:
        ans+=k//el
        k%=el
    print(ans)