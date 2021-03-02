import sys; input= lambda: sys.stdin.readline().rstrip()
n= int(input())

dp= [[1e9]*n for _ in range(n)]
for i in range(n):
    tmp= [*map(int, input().split())]
    for idx, el in enumerate(tmp):
        if el:
            dp[i][idx]= el


# 한번갔던 도시로는 다시 갈 수 없다..
'''
for i in range(n):
    for j in range(n):
        for k in range(n):
            dp[j][k]= min(dp[j][k], dp[j][i]+ dp[i][k])
'''
chk= [False]*n
ans=1e9
def dfs(v, cost):
    #print(v, chk, cost)
    global ans
    if all(chk[1:]):
        ans= min(ans, cost+dp[v][0])
    for i in range(1,n):
        if i!=v and not chk[i] and dp[v][i] and dp[v][i]<1e9:
            cost+=dp[v][i]
            chk[i]=True
            dfs(i,cost)
            chk[i]=False
            cost-=dp[v][i]


dfs(0,0)
print(ans)

# 반례 1 3 1 2 4
'''
4
0 5 1 99
99 0 5 1
1 99 0 5
5 1 99 0
'''