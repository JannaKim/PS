import sys; input= lambda: sys.stdin.readline().rstrip()
from heapq import heappop, heappush
Dy= [0,0,1,-1]
Dx= [1,-1,0,0]
cnt=0
while True:
    cnt+=1
    n= int(input())
    if not n:
        break
    mp=[]
    for _ in range(n):
        mp.append([*map(int, input().split())])
    accum= [[1e9]*n for _ in range(n)]
    accum[0][0]=mp[0][0]
    q=[]
    heappush(q,(0,0,mp[0][0]))
    while q:
        y, x, c= heappop(q)
        if accum[y][x]<c:
            continue
        for dy, dx in zip(Dy, Dx):
            ny= y+dy
            nx= x+dx
            if 0<=ny<n and 0<=nx<n:
                if c+mp[ny][nx]<accum[ny][nx]:
                    accum[ny][nx]= c+mp[ny][nx]
                    heappush(q,(ny, nx, accum[ny][nx]))
    print(f'Problem {cnt}: {accum[n-1][n-1]}')

