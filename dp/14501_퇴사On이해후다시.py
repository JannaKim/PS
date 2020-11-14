N = int(input())
cn = [0]
for _ in range(N):
    cn.append([int(i) for i in input().split()])
cn += [[0,0]]
#dp[i]: i일 '전'에 끝나는 최상의 스케쥴
dp = [0]+ [0]*(N+2)
for i in range(1,N+2):
    if i+cn[i][0]<=N+1: # N+1일 '전'까지 끝날 수 있는 스케쥴만.
        dp[i+cn[i][0]]= max(dp[i+cn[i][0]], dp[i]+cn[i][1])
    # i+1 날은 더이상 비교할, i+1일 '직전'에 맞춰 끝나는 스케쥴이 없다. 
    # i+1일 직전에 맞추지 않아도 더 많은 금액을 받을 수 있는 스케쥴이 있을 수 있으므로
    #dp[i+1]=max(dp[1:i+2])
    dp[i+1]=max(dp[i+1],dp[i])

print(max(dp[:N+2]))

'''
7
3 10
5 20
1 10
1 20
2 15
4 40
2 200
'''