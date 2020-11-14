n = int(input())
dp = [0] * (n+1)
*K,  = map(int, input().split())
for k in K:
    dp[k] = dp[k - 1] + 1 # 자기보다 뒤에있으면 1, 앞에있으면 연결
print(n - max(dp))