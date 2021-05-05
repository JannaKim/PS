s= int(input())
dp= [1e9]*(s+5)
dp[1]=0
#dp[i]: i개 만드는 최소시간
for i in range(1,s+4):
    for j in range(1,i+1):
        if not i%j:
            dp[i]= min(dp[i], dp[i//j]+j)
            dp[i-1]= min(dp[i-1], dp[i//j]+j+1)
            if i-2>=1:
                dp[i-2]= min(dp[i-2], dp[i//j]+j+2)
            if i-3>=1:
                dp[i-3]= min(dp[i-3], dp[i//j]+j+3)

print(dp[s])