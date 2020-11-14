N = int(input())
cn=[[0,0]]
sv=[]
for i in range(1,N+1):
    cn.append([int(_) for _ in input().split()])
    sv.append([i+cn[i][0],i])
'''
for i in range(1,N+1):
    sv.append([i+cn[i][0],i])
'''


# dp[i]: i일 '전'까지 상담해서 얻을 수 있는 최대 수익
dp=[0]*(N+1)
''' 
# 이렇게 하면 dp가 순서대로 저장안된다.
for i in range(1,N+1):
    if i+cn[i][0] <= N:
        dp[i+cn[i][0]] = max(dp[i+cn[i][0]],cn[i][1]+ max(dp[:i+1]))
'''
sv.sort(key= lambda x:x[0])
for [a,b] in sv:
    if a<=N:
        dp[a] = max(dp[a],cn[b][1]+ max(dp[:b+1]))

# dp[i]: i일 '까지' 상담해서 얻을 수 있는 최대 수익
for i in range(1,N+1):
    if i+cn[i][0]<=N+1:
        dp[i]+=cn[i][1]

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


4
1 1
3 1
1 1
1 1

'''