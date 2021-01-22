import sys; input= lambda: sys.stdin.readline().rstrip();r=range
n, m= map(int, input().split())
dp=[0]*(m+1)
for _ in r(1,n+1):
    cur=[*map(int, input().split())]
    for i in r(1,m+1):
        dp[i]= max(dp[i],dp[i-1])+cur[i-1]
print(dp[m])


'''
mp=[0,0]
mp[0]=[0]*(m+1)
for i in r(1,n+1):
    mp[i%2]=[0]+[*map(int, input().split())]
    for j in r(1,m+1):
        mp[i%2][j]+=max(mp[(i%2)^1][j], mp[(i%2)^1][j-1], mp[i%2][j-1])
print(mp[n%2][m])
'''