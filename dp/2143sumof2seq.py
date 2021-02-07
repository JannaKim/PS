t= int(input())
A= int(input())
a= [*map(int, input().split())]
B= int(input())
b= [*map(int, input().split())]


a+=b

dp = []
for _ in range(t+1):
    dp.append([0]*(A+B+1))

for i in range(1, A+B+1):
    for j in range(1,t+1):

        if a[i]<=j:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-a[i]]+1)
        else:
            dp[i][j] = dp[i-1][j]
print(dp[A+B][t])