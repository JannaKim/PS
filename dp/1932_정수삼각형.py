n = int(input())
#dp[i][1~i]: i층의 [1~i]가 도착지점일때 최대합

dp=[[int(input())]]
for i in range(1,n):
    ints=[int(_) for _ in input().split()]
    dp.append([dp[i-1][0]+ints[0]])
    for j in range(1,i):
        dp[i].append(max(dp[i-1][j-1], dp[i-1][j])+ints[j])
    dp[i].append(dp[i-1][i-1]+ints[-1])
print(max(dp[i]))

'''
2차원 배열 한번에 append 못하면,
첫 append는 dp.append([])
다음부턴 dp[i].append()
'''