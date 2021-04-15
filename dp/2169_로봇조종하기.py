import sys; input= lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(100000)
n, m= map(int, input().split())
mars=[[*map(int, input().split())] for _ in range(n)]
#1: dfs TLE

NINF= -1e9
Dy= [0,-1,0] # 0왼에서옴, 1 아래에서옴, 2 오에서옴
Dx= [-1,0,1]
dp= [[[-NINF]*m for _ in range(n)] for _ in range(3)]
for i in range(m): 
    dp[2][0][i]=-NINF+1# 오른쪽에서 오는건 없다
    #dp[1][0][i]=dp[0][0][i-1]+mars[0][i]
    #dp[0][0][i]=dp[0][0][i-1]+mars[0][i]# 왼에서 오는건 그냥 누적이다

def topdown(y,x,d):
    #print(y,x,d)
    if y+x==0:
        return mars[0][0]
    if dp[d][y][x]!=-NINF:
        return dp[d][y][x]

    #print(y,x,d,'make')
    mx=NINF # 이거 0 으로 해준 게 문제였음
    for dir, (dy, dx) in enumerate(zip(Dy, Dx)):
        if 2-dir==d and dir!=1:
            continue
        # 1. 여기서 y==0 & ~ continue 이상한 구문
        ny= y+dy
        nx= x+dx
        if 0<=nx and nx<m and 0<=ny and ny<n:
            mx= max(topdown(ny,nx,dir), mx)
    dp[d][y][x]=mx+mars[y][x]
    #dp[1][y][x]=max(dp[1][y][x], dp[d][y][x])
    #print(y,x,d,dp[d][y][x],'made')
    return dp[d][y][x]

print(topdown(n-1,m-1,1))
#[[print(*i) for i in el] for el in dp]