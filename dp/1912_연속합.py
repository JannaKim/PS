N = int(input())
L = [int(i) for i in input().split()]
# dp[i]: L[i]를 마지막으로 포함시킨 최대합
dp=[L[0]]
for i in range(1,N):
    dp.append(max(dp[i-1]+L[i],L[i]))

print(max(dp))