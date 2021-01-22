import sys; sys.setrecursionlimit(100000)

def topdown(v):
    if dp[v] != None:
        return dp[v]
    
    dp[v]= dur[v]+ (max(topdown(el) for el in edge[v]) if edge[v] else 0)
    return dp[v]

for _ in range(int(input())):
    n, k= map(int, input().split())
    dur=[-1]+[*map(int, input().split())]
    edge=[[] for _ in range(n+1)]

    for _ in range(k):
        a, b= map(int, input().split())
        edge[b].append(a)


    dp=[None]*(n+1)
    goal= int(input())
    print(topdown(goal))