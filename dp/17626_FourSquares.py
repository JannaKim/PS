sq_num=[]
n=int(input())

for i in range(1,n+1):
    if i**2<=n:
        sq_num.append(i**2)
    else:
        break

dp=[0]+[1e9]*n

for i in range(n+1):
    for el in sq_num:
        if i+el<=n:
            dp[i+el]=min(dp[i]+1, dp[i+el])
print(dp[n])