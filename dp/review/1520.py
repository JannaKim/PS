import sys; input= lambda: sys.stdin.readline().rstrip()
m ,n = map(int, input().split())
r= range
mp=[]
mp=[[-1]*(n+2)]
mp+=[[-1]+[*map(int, input().split())]+[-1] for _ in r(m)]
mp+=[[-1]*(n+2)]

#[print(*el) for el in mp]
dp= [[-1]*(n+2) for _ in r(m+2)]

dp[1][1]= 1
#[print(*el) for el in dp]

def topdown(i,j):
    if dp[i][j]!=-1:
        return dp[i][j]
    a=b=c=d=0
    if mp[i-1][j]>mp[i][j]:
        a=topdown(i-1,j)
    if mp[i][j-1]>mp[i][j]:
        b=topdown(i,j-1)
    if mp[i][j+1]>mp[i][j]:
        c=topdown(i,j+1)
    if mp[i+1][j]>mp[i][j]:
        d=topdown(i+1,j)

    dp[i][j]= a+b+c+d
    return dp[i][j]


print(topdown(m,n))
