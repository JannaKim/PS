n, m = map(int, input().split())
board = [[*map(int, input().split())] for _ in range(n)]

k = int(input())

dp = [ [0] * m for _ in range(n)]

def bound(y, x):
    global n, m
    if y < 0 or y >= n:
        return False
    if x < 0 or x >= m:
        return False
    return True

for i in range(n):
    for j in range(m):
        if bound()
