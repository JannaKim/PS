t = int(input())
dp=[1, 1, 2, 4]+[-1]*70
for i in range(4,70):
    dp[i] = dp[i-1]+dp[i-2]+dp[i-3]+dp[i-4]

for _ in range(t):
    print(dp[int(input())])

'''
8
0
1
2
3
4
5
30
67
'''