n= int(input())
L= [*map(int, input().split())]
dp=[0]*n
for i in range(n):
    dp[i]=1 # 이거 안해노면 자기자신꺼 이프문에서 흡수가 안됨
    for j in range(i, -1, -1): # i-1로하면 dp[0]에서 문제됨. 이프문으로 해결하기.
        if L[j]<L[i]:
            dp[i]= max(dp[i], dp[j]+1)
print(max(dp))