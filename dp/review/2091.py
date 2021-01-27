import sys; input= lambda: sys.stdin.readline().rstrip()
r=range
L= [*map(int, input().split())]
x=L[0]
hi=L[1:]
unit= [1, 5, 10, 25]

nums=[0]*5
dp=[[0]*5 for _ in r(x+1)]
for idx, coin in enumerate(unit):
    for i in r(x, -1, -1):
        if dp[i][4] or i==0:
            for amount in r(1, hi[idx]+1):
                if i+coin*amount<=x:
                    if dp[i+coin*amount][4]<dp[i][4]+amount:
                        dp[i+coin*amount][4]=dp[i][4]+amount
                        for j in range(4):
                            dp[i+coin*amount][j]=dp[i][j]
                        dp[i+coin*amount][idx]+=amount
print(*dp[x][:-1])


