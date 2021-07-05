from collections import deque

n = int(input())


dp = [False] * (n + 1)

def bfs(num):
    q = deque()
    q.append((num, 0))
    while q:
        num, k = q.popleft()
        if num == 1:
            return k
        if not (num % 3) and not dp[num//3]:
            dp[num//3] = True
            q.append((num//3, k + 1))
        if not (num % 2) and not dp[num//2]:
            dp[num//2] = True
            q.append((num//2, k + 1))
        q.append((num - 1, k + 1))

print(bfs(n))
