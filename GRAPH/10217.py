from heapq import heappush, heappop
import sys
input= lambda: sys.stdin.readline().rstrip()
# ['', '', 'heappush(q, el)', 'heappop(q)']
t= int(input())
for _ in range(t):
    n, m, k= map(int, input().split())

    edge= [[] for _ in range(n+1)]

    for _ in range(k): 
        a, b, cost, dur= map(int, input().split())
        edge[a].append((dur, cost, b))




    shortest= [[int(1e9) for _ in range(m+1)] for __ in range(n+1)] #
    # shortest[i][j]: shortest dur time when cost= j, for airport i 
    #shortest[1] = [0 for _ in range(m+1)]
    shortest[1][0]= 0

    q=[(0,0,1)] # dur, cost, v
    
    ans=-1
    while q:
        d, c, v= heappop(q)
        if shortest[v][c]<d:  
            continue
        if v==n:
            ans=d
            break
        for dur, cost, v2 in edge[v]:
            if c+cost>m: continue
            if shortest[v2][c+cost]<=d+dur: continue
            for i in range(c+cost, m+1):
                if shortest[v2][i]>d+dur:
                    shortest[v2][i]= d+ dur
                else: break
            heappush(q, (shortest[v2][c+cost], c+ cost, v2))
    print('Poor KCM' if ans==-1 else ans)
'''
    ans= min(shortest[n][1:])
    if ans>=int(1e9): print('Poor KCM')
    else: print(ans)
'''

        
'''
https://www.acmicpc.net/problem/10217
'''

'''
import sys

input = sys.stdin.readline
flush = sys.stdout.flush


for _ in range(int(input())):
    n, m, k = map(int, input().split())
    nbhd = [[] for _ in range(n + 1)]
    for _ in range(k):
        a, b, c, d = map(int, input().split())
        nbhd[a].append((b, c, d))
    dp = [[10**9] * (m + 1) for _ in range(n + 1)]
    dp[n] = [0] * (m + 1)
    for j in range(1, m + 1):
        for i in range(1, n + 1):
            for b, c, d in nbhd[i]:
                if c <= j and dp[i][j] > dp[b][j - c] + d:
                    dp[i][j] = dp[b][j - c] + d

    if dp[1][m] == 10**9:
        print("Poor KCM")
    else:
        print(dp[1][m])


'''