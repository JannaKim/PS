from sys import *; input = lambda: stdin.readline().rstrip()
n = int(input())
L = [int(i) for i in input().split()]
dp=[-1]*n
for i in range(n):
    dp[i]=max(dp[i-1]+L[i], L[i])
print(max(dp))
