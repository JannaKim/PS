MIS = lambda: map(int,input().split())

n, m, k = MIS()
grid = [list(MIS()) for i in range(n)]
for d in range(min(n,m)//2):
    slot = []
    for i in range(d,n-d): 
        # print(i , d)
        slot.append((i, d, grid[i][d]))
    for j in range(d+1,m-d): 
        # print(j)
        slot.append((n-d-1, j, grid[n-d-1][j]))
    print(slot)
    for i in range(n-d-2,d-1,-1): slot.append((i, m-d-1, grid[i][m-d-1]))
    print(slot)
    for j in range(m-d-2,d,-1): slot.append((d, j, grid[i][j]))
    print(slot)
    for x in range(len(slot)):
        i, j, d = slot[(x+k) % len(slot)]
        grid[i][j] = slot[x][2]

for row in grid: print(*row)