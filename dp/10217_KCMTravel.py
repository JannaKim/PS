import sys

input = lambda: sys.stdin.readline().rstrip()
flush = sys.stdout.flush


for _ in range(int(input())):
    n, m, k = map(int, input().split())
    nbhd = [[] for _ in range(n + 1)]
    for _ in range(k):
        a, b, c, d = map(int, input().split())
        nbhd[a].append((b, c, d)) # dest, cost, dur
    dp = [[10**9] * (m + 1) for _ in range(n + 1)]
    dp[n] = [0] * (m + 1)
    for j in range(1, m + 1):
        for i in range(1, n + 1):
            for b, c, d in nbhd[i]:
                #print(b, c, d)
                if c <= j and dp[i][j] > dp[b][j - c] + d:
                    dp[i][j] = dp[b][j - c] + d
                    #print(f'dp[{i}][{j}] = dp[{b}][{j - c}] + {d}')
    print(dp[1])
    if dp[1][m] == 10**9:
        print("Poor KCM")
    else:
        print(dp[1][m])