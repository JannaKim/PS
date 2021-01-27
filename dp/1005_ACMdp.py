def search(target):
    
    if dp[target] or cost[target-1] == 0:
        return dp[target]

    max_cost = 0

    for i in range(1, n+1):
        if rules[i][target]:
            max_cost = max(max_cost, search(i))
    dp[target] = max_cost + cost[target-1]
    return dp[target]



for _ in range(int(input())):
    n, k = map(int, input().split())
    dp = [0]*(n+1)
    rules = [ [0]*(n+1) for _ in range(n+1)]
    cost = list(map(int, input().split()))
    for _ in range(k):
        x, y = map(int, input().split())
        rules[x][y] = 1
    target = int(input())
    print(search(target))