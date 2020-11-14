N=int(input())
#dp[i]=dp[i-1]+dp[i-2]
a, b=1,2
if N==1:
    print(a)
elif N==2:
    print(b)
else:
    K=0
    for i in range(3,N+1):
        K=(b+a)%15746
        a,b=b,K

    print(K) #K%15746 시간초과?

#https://www.acmicpc.net/problem/1904