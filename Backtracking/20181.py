import sys
sys.setrecursionlimit(100005)

# Input
n, k = map(int, sys.stdin.readline().strip().split())
food = list(map(int, sys.stdin.readline().strip().split()))
food.insert(0, 0)

ans = 0
def dfs(idx: int, energy: int):
    print(idx,energy)
    global ans
    ans = max(ans, energy)
    if idx == n:
        return
    
    sum = 0
    for i in range(idx, n):
        sum += food[i]
        if sum >= k:
            dfs(i + 1, energy + (sum - k))
            break

    dfs(idx + 1, energy)

#N =9 K 6
#7 7 7 7 7 7 7 7 7 : 2**9 ?
dfs(0, 0)
print(ans)

'''
200 5
10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10
'''