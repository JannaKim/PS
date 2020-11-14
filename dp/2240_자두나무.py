T, W = map(int, input().split())
p = [0]
for _ in range(T):
    p.append(int(input()))

#dp[i][j]: i번 움직였을 때 j초동안 자두가 받을 수 있는 최대 자두 개수

#dp[i][j][k] i초동안 최대 j번 움직였을 때 받을 수 있는 최대 자두 개수. 나무의 위치
dp = []

for i in range(T+1):   
    dp.append([]) 
    [dp[i].append([0,0])  for _ in range(W+1)]
S = [[[0,0] for _ in range(W + 1)] for _ in range(T + 1)]

#[[[0,0],[0,0] ,...,[0,0] ,[0,0]]*(T+1) ,  ,  ,]*(W+1)
[print(i) for i in dp]
[print(i) for i in S]

'''
for i in range(1, T+1):
    if p[i]==1:
        dp[i][0][0]=dp[i-1][0][0]+1
    else:
        dp[i][0][0]=dp[i-1][0][0]
'''

#print(dp)
mx = 0
for i in range(1,T+1): # i초동안
    for j in range(W+1): #최대 j번 움직였을 때
        #if j==0:
        #    dp[i][j][1]=0
        if p[i]==1:
            if j!=0:
                # i-1초동안 최대 j번 움직였을때 마지막 위치 0
                dp[i][j][0]=max(dp[i-1][j][0]+1,dp[i-1][j-1][1]+1)
                # i-1초동안 최대 j번 움직였을때 마지막 위치 1
                dp[i][j][1]=max(dp[i-1][j-1][0], dp[i-1][j][1])
            elif j==0:
                dp[i][j][1]=0
                if p[i]==1:
                    dp[i][j][0]= dp[i-1][j][0]+1
                else:
                    dp[i][j][0]= dp[i-1][j][0]
        else: # p[i]==2:
            if j!=0:
                dp[i][j][1]=max(dp[i-1][j][1]+1,dp[i-1][j-1][0]+1)
                dp[i][j][0]=max(dp[i-1][j][0], dp[i-1][j-1][1])
            elif j==0:
                dp[i][j][1]=0
                if p[i]==1:
                    dp[i][j][0]= dp[i-1][j][0]+1
                else:
                    dp[i][j][0]= dp[i-1][j][0]
        mx = max([mx, dp[i][j][0], dp[i][j][1]])
        
        #print(f'dp[{i}][{j}] {dp[i][j]}')

# 2나무에 시작하는 경우ㅡ 생각할 필요없다 ?


        
print(mx)
'''
7 2
2
1
1
2
2
1
1
'''












'''
for j in range(1, T+1):
    if p[j]==1:
        dp[0][j]=dp[0][j-1]+1
    else:
        dp[0][j]=dp[0][j-1]

for i in range(1,W+1):
    for j in range(i,T+1):
        if i%2: #나무 2에 위치
            if p[j]==2:
                dp[i][j]=dp[i-1][j]+1
            else:
                dp[i][j]= dp[i-1][j-1]
        else: #나무 1에 위치
            if p[j]==1:
                dp[i][j]=dp[i-1][j]+1
            else:
                dp[i][j]= dp[i-1][j-1]

for i in range(1,T+1)
'''
#[print(i) for i in dp]
#print(dp[-1][-1])

'''
7 2
2
1
1
2
2
1
1
'''