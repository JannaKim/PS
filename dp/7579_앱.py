import math
N, M = map(int, input().split())
L=[int(i) for i in input().split()]
C=[int(i) for i in input().split()]

dp=[0 for _ in range(101*N+1)]

mn= math.inf
#dp[0][1~10000]

#dp[i]: 
for i in range(N): #비용 j썼을때 얻을 수 있는 최대 메모리
    for j in range(101*N,-1,-1):
        if j>=C[i]:
            if dp[j-C[i]]>0 or j==C[i]:
                dp[j]= max(dp[j-C[i]]+L[i], dp[j])
    

for i in range(101*N):
    if dp[i]>=M:
        print(i)
        break