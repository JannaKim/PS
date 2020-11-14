N = int(input())
L = [0] +[int(i) for i in input().split()]

#dp[i]: i 번째 어린이까지 줄 세웠을 떄 앞이나 뒤로 보내는는 최소횟수
dp = [0]*(N+1)
dp[1]=0
mn=1e7
mx=-1
for i in range(2,N+1):
    if L[i-1]<L[i]: # 전, 지금 오름차순일 때
        dp[i]= min(dp[i-2]+mx-L[i], 2)
    else: #내림
        if mx==L[i]:
            dp[i]= dp[i-1]+1
        else:
            dp[i]=dp[i-1]+1

    mx = max(mx, L[i])
    mn = min(mn, L[i])
    print(dp[i])



print(dp[N-1])



n = int(input())
dp = [0] * (n+1)
*K,  = map(int, input().split())

for k in K:
    dp[k] = dp[k - 1] + 1
    
print(n - max(dp))

'''
8
4 2 3 1 5 7 6 8

5
5 2 4 1 3
'''