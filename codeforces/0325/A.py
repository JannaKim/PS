import sys; input= lambda: sys.stdin.readline().rstrip()

for _ in range(int(input())):
    n, m, x= map(int, input().split())
    x-=1
    i= x%n
    j= x//n
    ans= i*m+j
    print(ans+1)