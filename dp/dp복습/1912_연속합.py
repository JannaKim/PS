# dp[i]: i째 수열로 끝나는 최대합

n = int(input())
L = list(map(int,input().split()))

dp=[L[0]]+[0]*(n-1)
for i in range(1,n):
    dp[i]=max(dp[i-1]+L[i], L[i])
print(max(dp))


'''
10
10 -4 3 1 5 6 -35 12 21 -1
'''

