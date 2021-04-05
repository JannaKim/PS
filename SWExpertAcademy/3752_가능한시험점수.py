import sys; f=sys.stdin
mx=100**2
T=int(input())
for t in range(1,T+1):
    n= int(input())
    L=[*map(int,input().split())]

    dp= [1]+[0]*mx
    for score in L:
        for i in range(mx,-1,-1):
            if dp[i]:
                dp[i+score]=1
    print(f'#{t} {sum(dp)}')