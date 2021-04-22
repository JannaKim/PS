n, s= map(int, input().split())
seq= [0]+[*map(int, input().split())]
dp=[0]*(n+1)
for i in range(1,n+1):
    dp[i]=dp[i-1]+seq[i]

cnt=0
for i in range(1,n+1):
    for j in range(i):
        print(i, j)
        if dp[i]-dp[j]==s:
            cnt+=1
print(cnt)