T, W = map(int, input().split())
plum=[0]+[int(input())-1 for _ in range(T)]

#dp[i][j][k]: 최대 자두, i초동안 최대 j번 움직였을 때 마지막 위치k
#dp[T][W][1]
dp=[[[0]*2 for _ in range(W+1)] for __ in range(T+1)]
for i in range(1,T+1):
    dp[i][0]=dp[i-1][0]
    dp[i][0][plum[i]]+=plum[i]^1
    for j in range(1,W+1):
        dp[i][j][plum[i]]=max(dp[i-1][j][plum[i]]+1, dp[i-1][j-1][plum[i]^1]+1)
        dp[i][j][plum[i]^1]=max(dp[i-1][j][plum[i]^1], dp[i-1][j-1][plum[i]])
mx = 0

print(max(dp[T][W]))


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
        

