n=int(input())
P= [*map(int, input().split())]
dp = [0] * n
dp[0]=P[0]


for i in range (1,n):
    if dp[i-1] >= 0:
        dp[i]=P[i]+dp[i-1]#P[-1]이 들어감
    else:
        dp[i]=P[i]
print(max(dp))