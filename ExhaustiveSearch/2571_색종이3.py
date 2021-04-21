import sys; input= lambda: sys.stdin.readline().rstrip()
n= int(input())
dp= [[0]*100 for _ in range(100)]
for _ in range(n):
    y,x= map(int, input().split())
    for i in range(y,y+10):
        for j in range(x,x+10):
            dp[i][j]=1

for i in range(100):
    for j in range(100):
        if dp[i][j] and j>=1:
            dp[i][j]=dp[i][j-1]+1
ans=0
for i in range(99,-1,-1):
    for j in range(100):
        if (j==0 and dp[j][i]) or (dp[j-1][i]!=dp[j][i] and dp[j][i]):
            w= dp[j][i]
            a=j
            b=j
            while dp[b][i]>=w:
                b-=1
                if b==-1:
                    break
            b+=1
            while dp[a][i]>=w:
                a+=1
                if a==100:
                    break
            ans=max(ans,w*(a-b))
print(ans)