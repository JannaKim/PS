import sys; input= lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(1000000)
n= int(input())
edge= [[] for _ in range(n+1)]

for _ in range(n-1):
    u, v= map(int, input().split())
    edge[u].append(v)
    edge[v].append(u)

dp= [[1e9]*2 for _ in range(n+1)]
def topdown(v,v1):
    if dp[v][0]!=1e9:
        return dp[v]
    dp[v][0] = 0
    dp[v][1] = 1
    for v2 in edge[v]:
        if v2==v1:
            continue
        dp[v][0]+= topdown(v2,v)[1]
        dp[v][1]+= min(topdown(v2,v)[0], topdown(v2,v)[1])
    
    return dp[v]

print(min(topdown(1,0)))
#[print(el) for el in dp]



'''
q=[]
[heappush(q,indegree[i]) for i in range(1,n+1)]
cnt=0
while q:
    deg, v= heappop(q)
    if indegree[v][0]!=deg:
        heappush(q,indegree[v])
        continue
    if not deg: break
    cnt+=1
    for v2 in edge[v]:
        indegree[v2][0]+=1

print(cnt)
'''