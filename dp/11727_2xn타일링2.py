dp = [0,1,3]
#dp[i]: 2*i 사각형을 채우는 방법의 수
#dp[i]= dp[i-1]+dp[i-2]*2
n = int(input())
if n<=2:
    print(dp[n])
else:
    for i in range(3,n+1):
        dp.append(dp[i-1]+dp[i-2]*2)
    print(dp[n]%10007)