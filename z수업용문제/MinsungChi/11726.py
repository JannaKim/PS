import sys
for el in sys.stdin:
    n=int(el)
    if n==0 or n== 1:
        print(1)
    else:
        dp=[]
        dp=[0]*(n+1)
        dp[0]=1
        dp[1]=1
        dp[2]=3
        for i in range(3,n+1):
            dp[i]=(dp[i-1]+dp[i-2]*2)
        print(dp[n])
