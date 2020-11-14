T = int(input())
for _ in range(T):
    N = int(input())
    won = [int(i) for i in input().split()]
    P = int(input())
    dp=[1]+[0]*P
    for i in won:
        for j in range(i,P+1):
            dp[j]+=dp[j-i]
    print(dp[P])

'''
3
2
1 2
1000
3
1 5 10
100
2
5 7
22
'''