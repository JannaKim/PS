n=int(input())
L=[]
for i in range (n):
    a=int(input())
    L.append(a)


dp = []
for _ in range(n):
    dp.append([0,0])

# dp[i][0] : 첫 밟 : 최대점수
# dp[i][1] : 두번째 연속 밟 : 최대 점수
for i in range (1,n):
    dp[i][0] = L[i]+max(dp[i-2][0],dp[i-2][1])
    dp[i][1] = L[i] + dp[i-1][0]

print(max(dp[n-1]))



