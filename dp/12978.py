import sys; input= lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(100000) 
n= int(input())
edge= [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b= map(int, input().split())
    edge[a].append(b)
    edge[b].append(a)

dp= [[0]*2 for _ in range(n+1)]

def topdown(v, v1):
    #print(v,v1)
    dp[v]= [0,1]
    for v2 in edge[v]:
        if v2==v1:
            continue
        ths= topdown(v2,v)
        dp[v][0]+= ths[1]
        dp[v][1]+= min(ths[0], ths[1])

    return dp[v]


print(min(topdown(1,0)))