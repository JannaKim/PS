from collections import deque
I= input; r=range
t= int(I())
for _ in r(t):
    n, k= map(int, I().split())
    time = [0]+ [*map(int, I().split())]
    edge= [[] for _ in r(n+1)]
    for _ in r(k):
        a, b= map(int, I().split())
        edge[b].append(a)
    goal= int(I())
    dp=[0 for _ in r(n+1)]
    dp[goal]=time[goal]
    
    q= deque()
    q.append(goal)
    while q:
        v= q.popleft()
        for v2 in edge[v]:
            if dp[v2]<dp[v]+time[v2]:
                dp[v2]=dp[v]+time[v2]
                q.append(v2)

    print(max(dp[1:])) 