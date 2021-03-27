wire= [0]*501
for _ in range(int(input())):
    a, b= map(int, input().split())
    wire[b]=a

L=[]

for i in range(1,1+500):
    if wire[i]:
        L.append(wire[i])

Len= len(L)

dp= [1]*Len
#dp[i]: i 번째로 끝나는 최장 증가수열의 길이
for i in range(Len):
    for j in range(i,-1,-1):
        if L[j]<L[i]:
            dp[i]=max(dp[j]+1,dp[i])

print(Len-max(dp))