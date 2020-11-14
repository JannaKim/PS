n = int(input())

w = []
for _ in range(n):
    w.append(int(input()))


# dp[i][0]: i잔을 안마심
# dp[i][1]: i잔을 한번 연속으로 마심
# dp[i][2]: i잔을 두번 연속으로 마심

dp = [[0]*3 for _ in range(n)]

dp[0]=[0,w[0],w[0]]

for i in range(1,n):
    dp[i]= [max(dp[i-1]), dp[i-1][0] + w[i], dp[i-1][1] + w[i]]
    

print(max(dp[n-1]))


'''
6
6
10
13
9
8
1
'''