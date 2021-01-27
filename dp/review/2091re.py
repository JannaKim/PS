coffee, *num, = [*map(int, input().split())]
units=[1, 5, 10, 25]

r= range
dp= [[0]*5 for _ in r(coffee+1)]
for i, unit in enumerate(units):
    for j in r(coffee, -1, -1):
        for getsoo in r(1,num[i]+1):
            if j==0 or dp[j][4]:
                if j+unit*getsoo<=coffee:
                    if j==0 or dp[j+unit*getsoo][4]<dp[j][4]+getsoo:
                        dp[j+unit*getsoo][4]= dp[j][4]+getsoo
                        for k in r(4):
                            dp[j+unit*getsoo][k]= dp[j][k]
                        dp[j+unit*getsoo][i]+=getsoo
print(*dp[coffee][:-1])