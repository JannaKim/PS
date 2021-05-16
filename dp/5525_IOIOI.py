n= int(input())
m=int(input())
L= input()
dp=[0]*m
for i in range(2,m):
    if L[i-2]+L[i-1]+L[i]=='IOI':
        dp[i]=dp[i-2]+1
ans=0
for i in range(m):
    if dp[i]>=n:
        ans+=1
print(ans)

    
