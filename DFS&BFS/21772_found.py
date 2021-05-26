import sys

input = sys.stdin.readline

R, C, T = map(int, input().split())

grid = [list(input().rstrip()) for i in range(R)]

direction = ((1, 0), (0, 1), (-1, 0), (0, -1))

S = [[*j] for j in grid]
visited = [[False for i in range(C)] for i in range(C)]
answer = [0]

def dfs(i, j, t, n):
    if grid[i][j] == "S":
        n += 1
    answer[0] = max(answer[0], n)
    if t == T:
        return

    # print(i, j, t, n)
    for idx in range(4):
        di, dj = direction[idx]
        ni, nj = i + di, j + dj
        if 0 <= ni < R and 0 <= nj < C and grid[ni][nj] != '#' and visited[ni][nj] == False:
            visited[ni][nj] = True
            dfs(ni, nj, t + 1, n)
            visited[ni][nj] = False



for i in range(R):
    for j in range(C):
        if grid[i][j] == 'G':
            dfs(i, j, 0, 0)
            print(answer[0])