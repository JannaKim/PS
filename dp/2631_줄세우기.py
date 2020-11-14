import sys; input= lambda:sys.stdin.readline().rstrip()
N = int(input())
L =[int(input()) for _ in range(N)]
# dp[i]: i번째를 끝으로 하는 최장 증가수열
dp=[1]*(N+1)
for i in range(N):
    for j in range(i):
        if L[i]>L[j]:
            dp[i]=max(dp[i], dp[j]+1)
#print(dp)
print(N-max(dp))

'''
7
3
7
5
2
6
1
4
'''