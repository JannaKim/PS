N = int(input())
# dp[i]: i를 1로 만드는 데 필요한 최소 연산 수
#처음에 /3 한 경우, 처음에 /2 한 경우, 처음에 -1 한 경우 로 나뉜다
dp=[]
dp=[-1,0]
for i in range(2,N+1):
    a=b=c=0
    if i%3==0:
        a=i//3
    if i%2==0:
        b=i//2
    c=i-1
    dp.append(min(dp[a]+1,dp[b]+1,dp[c]+1))



print(dp[N])