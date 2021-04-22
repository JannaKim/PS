import sys; input= lambda: sys.stdin.readline().rstrip()
n, m= map(int, input().split())
ans=1
for i in range(1,m+1):
    ans*=(n-i+1)
    ans//=i
print(ans)