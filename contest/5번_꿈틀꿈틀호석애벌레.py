N, K = map(int, input().split())
L = [0]+[int(i) for i in input().split()]

dp=[0]*(N+1)
#dp[i]: i번째까지 얻을 수 있는 최대 만족도
for i in range(1,N+1):
    if L[i]<K:
        s=L[i]
        stop=0
        for j in range(i+1,N+1):
            s+=L[j]
            if s>=K:
                stop=j
                break
            
        dp[stop] = max((dp[i-1] if i-1>0 else 0)+s-K,dp[stop])
    #print(f'dp[{stop}]: {dp[stop]}')
    dp[i]=max(dp[i],dp[i-1])
    #print(f'현재 dp[{i}]: {dp[i]}')

print(dp[N])
'''
9 6
1 5 4 4 2 3 10 3 5
'''