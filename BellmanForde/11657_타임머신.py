# dp[i]: st to i min dist
n , m = map(int, input().split())
edge = []
for _ in range(m):
    a , b , c = map(int, input().split())
    edge.append( (a , b , c))
dp = [1e9] * (n + 1)
dp[1] = 0
def BF():
    for t in range(1 , n + 1):
        for v  , v2 , cost in edge:
            if dp[v] != 1e9 and dp[v] + cost < dp[v2]:
                dp[v2] = dp[v]  + cost
                if t== n:
                    return False

                
    return True

if not BF():
    print(-1)
else:
    for v in range(2 , n + 1):
        print([dp[v] , -1][dp[v] == 1e9])
