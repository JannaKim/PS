# 0 , 0 -> n-1, n-1 로 이동해야 함. 
import sys
input = sys.stdin.readline
import heapq
INF = int(1e9)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
n = int(input())
count = 0
while True:
    count += 1
    if n == 0: # 종료 
        sys.exit(0)

    graph = []
    dist = [[INF]*n for _ in range(n)] # 0,0 -> n-1, n-1, 합이 가장 작아야 함. 
    for _ in range(n):
        graph.append(list(map(int, input().split())))
    
    dist[0][0] = graph[0][0] # start

    q = []
    heapq.heappush(q, (0, 0, dist[0][0])) # x, y, cost
    while q:
        x, y, d = heapq.heappop(q)
        print(x,y,d)
        if dist[x][y] < d:
            continue

        for i in range(n):
            nx = x + dx[i]
            ny = y + dy[i]
            print('n',nx,ny)

            if 0 <= nx < n and 0 <= ny < n:
                cost = d + graph[nx][ny]
                if cost < dist[nx][ny]:
                    dist[nx][ny] = cost
                    [print(*el) for el in dist]
                    heapq.heappush(q, (nx, ny, dist[nx][ny]))
 
    print(f'Problem {count}: {dist[n-1][n-1]}')