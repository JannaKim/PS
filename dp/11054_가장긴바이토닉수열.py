N = int(input())
A = [0]+ [int(i) for i in input().split()]

# dp[i]: A[i]로 끝나는 최장 증가수열 길이
dp=[0]+[1]*(N)
for i in range(1,N+1):
    for j in range(1,i):
        if A[i]>A[j]:
            dp[i] = max(dp[i], dp[j]+1)
    # dp[i] 완성



dp2=[0]+[1]*N
for i in range(N,0,-1):
    for j in range(N,i,-1):
        if A[i]>A[j]:
            dp2[i] = max(dp2[i], dp2[j]+1)

mx=0
for i in range(1,N+1):
    for j in range(i+1,N+1):
        if A[i]>A[j]:
            mx = max(mx, dp[i]+dp2[j])

mx = max(mx, dp[N], dp2[1]) # 증가만, 감소만이 최장일때 경우도 생각해준다.

print(mx)


'''
10
1 5 2 1 4 3 4 5 2 1
'''