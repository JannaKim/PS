import sys; input= lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(250000)
n= int(input())
edge= [[] for _ in range(n+1)]
for _ in range(n):
    line= [*map(int, input().split())]
    for j in range(1,n*2,2):
        if line[j]==-1:
            break
        edge[line[0]].append((line[j], line[j+1]))


dp= [0]*(n+1) # 자기 부터 아래로 뻗는 가장 긴 길이
def d(v, v1):
    mx=0
    for v2, cost in edge[v]:
        if v1!= v2:
            dp[v2]= d(v2, v)
            mx= max(mx, dp[v2]+cost)
    return mx

dp[1]= d(1, 0)

ans= 0
def dfs(v, v1, accum):
    global ans
     # 1자 길이
    #print(v, accum, prv)
    ans= max(ans, accum+dp[v])
    DP= [0,0]
    for v2, cost in edge[v]:
        if v2 !=v1:
            DP[0] = max(DP[0], cost+dp[v2])
            DP.sort()
    if len(DP)>1:
        DP.sort()
        ans= max(ans,sum(DP))
    del DP

    for v2, cost in edge[v]:
        if v2!=v1:
            dfs(v2, v, accum+cost)
#print(dp)
dfs(1, 0, 0)
print(ans)

'''
def dfs(v, accum, prv):
    #print(v, accum, prv)
    global mx
    dp= [0]*(len(edge[v])+1)
    for idx, (v2, cost) in enumerate(edge[v]):
        if v2!=prv:
            dp[idx]= max(dfs(v2, accum+cost, v), cost)

    dp.sort()
    #print(v, dp)
    mx= max(mx, accum+dp[-1])
    if len(dp)>=2:
        mx= max(mx, dp[-1]+dp[-2])
    
    return max(dp)

dfs(1, 0, 1)
print(mx)

'''
'''
cmd t
cmd 1
pwd
cmd space



5
1 3 2 -1
2 4 10 -1
3 1 2 4 3 -1
4 2 10 3 3 5 10 -1
5 4 10 -1

10
1 2 1 -1
2 3 1 -1
3 4 1 -1
4 5 1 -1
5 6 1 -1
6 7 1 -1
7 8 1 -1
8 9 1 -1
9 10 1 -1
10 -1

'''