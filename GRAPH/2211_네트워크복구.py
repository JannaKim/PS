from heapq import heappop , heappush
n , m = map(int, input().split())

edge = [ [] for _ in range(n + 1)]

for _ in range(m):
    a , b , cst = map(int , input().split())
    edge[a].append( (b, cst) )
    edge[b].append( (a , cst) )

q = []
heappush(q , (0 , 1) )
dp = [ [1e9, [] ] for _ in range(n + 1)]
dp[1][0] = 0

while q:
    cost , v = heappop(q)
    #print(cost , stc)
    if dp[v][0] < cost:
        continue

    for v2 , c in edge[v]:
        if cost + c < dp[v2][0]:
            dp[v2][0] = cost + c
            nxt = dp[v][1][:]
            nxt.append(v2)
            dp[v2][1] = nxt
            heappush(q , (dp[v2][0] , v2) )

ans = set()
for i in range(2 , n + 1):
    ans.add((1 , dp[i][1][0]))
    for a , b in zip(dp[i][1] , dp[i][1][1:]):
        ans.add( (a , b) )

print(len(ans))
[print(*el) for el in ans]

'''
a -> b 가 최단경로면
a -> c -> b일 때
a - > c도 최단경로다