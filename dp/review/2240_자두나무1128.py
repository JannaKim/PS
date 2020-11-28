T, W = map(int, input().split())
plum = [0]+ [int(input())-1 for _ in range(T)]
dp=[[0]*(W+1) for _ in range(T+1)]
#print(dp[0])
for t in range(1,T+1):
    for w in range(W+1):
        dp[t][w] = max(dp[t-1][w], dp[t-1][w-1] if w else -1)
        #print(f'dp[{t}][{w}]: {dp[t][w]} = mx({dp[t-1][w]},{dp[t-1][w-1]})')
        if w%2==plum[t]:

            dp[t][w]+=1
        #print(f'dp[{t}][{w}]: {dp[t][w]}')
    
print(max(dp[T]))
'''
7 2
2
1
1
2
2
1
1
'''