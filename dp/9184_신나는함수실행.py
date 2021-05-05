import sys; input= lambda: sys.stdin.readline().rstrip()
dp= [[[150 for _ in range(201)] for ___ in range(201)] for __ in range(201)]
sys.setrecursionlimit(10000)
zero= 100
def w(a, b, c):
    if dp[a][b][c]!=150:
        return dp[a][b][c]
    if a<=zero or b<=zero or c<=zero:
        dp[a][b][c]=1
        return dp[a][b][c]
    if a > zero+20 or b > zero+20 or c > zero+20:
        dp[a][b][c]=w(zero+20, zero+20, zero+20)
        return dp[a][b][c]
    elif a<b<c:
        dp[a][b][c]= w(a,b,c-1)+w(a, b-1, c-1) - w(a, b-1, c)
        return dp[a][b][c]
        
    else:
        dp[a][b][c]= w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        return dp[a][b][c]

while True:
    a, b, c= map(int, input().split())
    if a==-1 and b==-1 and c==-1:
        break
    print(f'w({a}, {b}, {c}) = {w(zero+a,zero+b,zero+c)}')