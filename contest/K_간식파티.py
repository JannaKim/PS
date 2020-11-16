N = int(input())
T = [int(input()) for _ in range(N)]
#dp[i]: i날 간식을 먹었을 때 최대 만족도
dp=[0]*N
dp[0]=T[0]
for i in range(1,N):
    for j in range(i-1,-1,-1):
        if T[j]<T[i]:
            dp[i]=max(dp[j],dp[i])
    dp[i]+=T[i]
print(max(dp))

'''
5
4
5
1
2
3

10
3
7
3
4
8
5
10
9
3
4
'''