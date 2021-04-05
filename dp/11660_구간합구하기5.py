import sys; input= lambda: sys.stdin.readline().rstrip()
n, m= map(int, input().split())
dp= [[0]*n for _ in range(n)]

L=[]
for i in range(n):
    L=[*map(int, input().split())]
    dp[i][0]=L[0]
    for j in range(1,n):
        dp[i][j]= dp[i][j-1]+L[j]

for _ in range(m):
    x1, y1, x2, y2= map(int, input().split())
    s=0
    for i in range(x1-1,x2):
        s+=dp[i][y2-1]-(dp[i][y1-2] if y1>=2 else 0)
    print(s)