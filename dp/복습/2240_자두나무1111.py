# dp[T][W]
# dp[t][w]: t초동안 w번 움직였을 떄 최대 자두
import sys; input=lambda: sys.stdin.readline().rstrip()
T, W = map(int, input().split())
plum=[0]+[int(input())-1 for _ in range(T)]
dp=[[0]*(W+1) for _ in range(T+1)]

for t in range(1,T+1):
    for w in range(W+1):
        dp[t][w]=max(dp[t-1][w], dp[t-1][w-1] if w>0 else 0)
        if w%2==plum[t]:
            dp[t][w]+=1
print(max(dp[T]))

'''
7 2
2
1
1
2
2
1
1
'''