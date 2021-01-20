import sys; input= lambda: sys.stdin.readline().rstrip()
n,k= map(int, input().split())
L=[*map(int, input().split())]
print(sorted(L)[k-1])