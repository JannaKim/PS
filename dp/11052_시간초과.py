#카드 i장 구매를 위해 지불해야하는 금액 최대값?
#dp[i]: (0,i+1)을 이용해 숫자 i를 만들 수 있는 모든 경우
n = int(input())
P=[0]
P+=[int(i) for i in input().split()]
dp=[[[0]],[[1]],[[1,1],[2]],[[2,1],[1,1,1],[3]]]
#print(dp)
for a in range(4,n+1):
    dp.append([[a]])
    for i in range(1,(a//2+1)): # 숫자 a=4를 만들수있는 경우의 수는 dp[2]들과 dp[2]들의 조합, dp[1]들과dp[3]들의조합
        #print(f"dp[{a}-{i}]")
        L=dp[a-i][:]
        M=dp[i][:]
        #print(f"dp[{a}]를 위해 {L},{M} 조합중")
        for j in L:
            for k in M:
                if j+k and k+j not in dp[a]: # 중복 안되게 어떻게?
                    dp[a].append(j+k)
#print(dp[a])
s=0
mx=0
for seq in dp[a]:
    for i in seq:
        s+=P[i]
    if mx<s:
        mx=s
    s=0
print(mx)

# https://www.acmicpc.net/problem/11052
