#dp[i][j][0]: i초까지 최대 j번 움직였을 때 받는 최대 자두, 나무 1
#dp[i][j][1]: i초까지 최대 j번 움직였을 때 받는 최대 자두, 나무 2

T, W = map(int, input().split()) # 초, 움직임 횟수
plum=[0]
for _ in range(T):
    plum.append(int(input()))

dp=[]
for i in range(T+1):
    dp.append([])
    [dp[i].append([0,0]) for _ in range(W+1)]

mx = 0
for i in range(1,T+1):
    if plum[i]==1:
        dp[i][0][0]=dp[i-1][0][0]+1
    else:
        dp[i][0][0]=dp[i-1][0][0]
    dp[i][0][1]=0
    for j in range(1,W+1):
        if plum[i]==1:
            dp[i][j][0]=max(dp[i-1][j][0]+1, dp[i-1][j-1][1]+1)
            dp[i][j][1]=max(dp[i-1][j][1], dp[i-1][j-1][0])
        else: # 나무 2
            dp[i][j][0]=max(dp[i-1][j][0], dp[i-1][j-1][1])
            dp[i][j][1]=max(dp[i-1][j][1]+1, dp[i-1][j-1][0]+1)
        mx=max(mx,max(dp[i][j]))
#[print(i) for i in dp]
print(mx)



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