# 100 * 10만 : 1000만
N, K = [int(i) for i in input().split()]

WT = [0]*(N+1)
val = [0]*(N+1)

for i in range(1,N+1):
    [WT[i], val[i]] = [int(i) for i in input().split()]

#print(WT,val)


dp=[]
for _ in range(N+1):
    dp.append([0]*(K+1))

# dp[i][0] : 무게합
# dp[i][1] : 가치
# dp[i][1~N] :  
# dp[i][j] : 물건 번호 1~i사이의 물건만 가져갈 때
#            무게합이 j 이하일 때의 최대가치


for i in range(1, N+1):
    for j in range(1,K+1):
        if WT[i]<=j: # 물건i 무게가 k보다 작을때
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-WT[i]]+val[i])
        else: 
            dp[i][j]=dp[i-1][j]

print(dp[N][K])

'''
4 7
6 13
4 8
3 6
5 12
'''






'''
dp[1] = [WT[1], val[1]] 
# 물품 수 만큼 포문 돌리니까 인덱스 에러 안날텐데?
for i in range(1,N+1):
    for j in range(1,i+1): # 가능한 건 순서대로 다 넣어버리니까 안됨
        if WT[i] + dp[j][0] <=K: # 현재 i의 무게와 현재 j의 무게합이 K를 안 넘을 때
            #print(WT[i], dp[j][0], K)
            if dp[i][1]<dp[j][1]+val[i]: # 가치가 더 크다면 바꾼다
                dp[i] = [WT[i] + dp[j][0], val[i]+dp[j][1]]
    if dp[i][1]<val[i]:
        dp[i] = [WT[i], val[i]] # 물건 i만 가져가는게 최대 가치일 수 있으므로


if dp[1][1]>K:
    dp[1]=[0,0]
dp.sort(key = lambda x:x[1])
print(dp[-1][1])
'''
'''
4 7
6 13
4 8
3 6
5 12


4 7
6 3
4 6
3 7
2 10

4 5
1 2
1 1
1 0
1 3
'''