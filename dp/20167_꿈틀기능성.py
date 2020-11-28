N, K = map(int, input().split())
L=[0]+[int(i) for i in input().split()]
dp=[0]*(N+1)
for i in range(1,N+1):
    s=0
    for j in range(i,N+1):
        s+=L[j]
        if s>=K:
            dp[j]= max(s-K+ dp[i-1], dp[j])
            break
    #print(f'dp[{j}]: {dp[j]}')   
    dp[i]=max(dp[i], dp[i-1])
    #print(f'dp[{i}]: {dp[i]}')   
print(dp[N])
        
'''
3 5
3 4 5

9 6
1 5 4 4 2 3 10 3 5
'''