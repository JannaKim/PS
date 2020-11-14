N = int(input())
'''
cn: consult
i: consulting date
cn[i][0]: duration
cn[i][1]: earning
'''
cn=[[0,0]]
for _ in range(N):
    cn.append([int(i) for i in input().split()])


# i일 상담으로 인해 바뀌는 것?
# dp[i]: i일 '전'까지 상담해서 얻을 수 있는 최대 수익

dp=[0]*(N+2)

for i in range(1,N+2):
    for j in range(1,i):
        if j+cn[j][0]<=i:
            dp[i]=max(dp[i],dp[j]+cn[j][1])

# dp[i]: i일 '까지' 상담해서 얻을 수 있는 최대 수익
'''
for i in range(1,N+1):
    if i+cn[i][0]<=N+1:
        dp[i]+=cn[i][1]
'''
#print(dp)
print(max(dp))

'''
7
3 10
5 20
1 10
1 20
2 15
4 40
2 200
'''