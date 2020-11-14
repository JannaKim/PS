T, W = map(int, input().split())
plum = [0]+[int(input())-1 for _ in range(T)]

#dp[i][j]: i초동안 j번움직였을 떄 최대 자두 개수
dp=[[0]*(W+1) for _ in range(T+1)]
for i in range(1,T+1):
    dp[i][0]=dp[i-1][0]
    if plum[i]==0:
        dp[i][0]+=1
    for j in range(1,W+1):
        dp[i][j]=max(dp[i-1][j], dp[i-1][j-1])
        if j%2==plum[i]:
            dp[i][j]+=1

print(max(dp[T]))