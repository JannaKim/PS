import sys; input = lambda: sys.stdin.readline().rstrip()
T, W = map(int, input().split())
p = [0]
[p.append(int(input())) for _ in range(T)]

#dp[T][W]
dp= [[0]*(W+1) for _ in range(T+1)]


#dp[i][j]: i초동안 j번 움직였을 때 자두가 받을 수 있는 최대 자두 개수

for i in range(1,T+1):
    #for j in range(1,i):
    dp[i][0]=dp[i-1][0]
    if p[i]==1:
        dp[i][0]+=1
    for j in range(1,W+1):
        dp[i][j]=max(dp[i-1][j], dp[i-1][j-1])
        if j%2==p[i]-1:
            dp[i][j]+=1

print(max(dp[-1]))

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