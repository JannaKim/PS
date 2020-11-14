import sys; input = lambda: sys.stdin.readline().rstrip()
T, W = map(int, input().split())
dp = [[0 for _ in range(W + 1)] for __ in range(T + 1)]
plum = [0]+[int(input()) - 1 for _ in range(T)]

# t초동안 w번 움직이는 것: max(t초 전에 w번 움직인 것 + 현 t초에서 w번쨰로 움직인것)
# w번 움직였다: 홀수번 움직였으면 나무 2에, 짝수번 움직였으면 나무 1에 위치해 있다.
# a초동안 a+1번 이상으로 움직이는 건 불가능하다.
# t<w 일 경우는 불가능하다. 하지만 가장 많은 자두를 받아야하므로 
# 이러한 움직이는 횟수를 줄여버린 경우은 max처리 과정에서 처리된다
# 그렇다면 최대 W번의 움직임으로 최소의 지두를 받아내는 경우라면?
# 이 때도 횟수를 줄여버린 경우이므로 min과정에서 처리된다
# 
# 무조건 W번 움직여서 최대의 자두를 받아내는 경우라면?
# t<w인 경우엔 t번이 최대로 움직이는 것.
# t<w일 때 dp[t][w]=0  
for t in range(1, T + 1):
    for w in range(W + 1):
        dp[t][w] = max(dp[t - 1][w], dp[t - 1][w - 1] if w > 0 else 0) # 0번 움직였을 때는 전에 것이 없다
        if w % 2 == plum[t]:
            dp[t][w] += 1
        if t<w:
            dp[t][w]=0

print(max(dp[T]))
