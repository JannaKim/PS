N, M = map(int,input().split()) # 변수에 따로받는건 list로 안감싸도되나
mp=[]
dp=[]
for i in range(N):
    dp.append([0]*M)
    mp.append(list(map(int,input().split()))) 
    # mp.append(0)
    # mp[i]=list(map(int,input().split()))

# dp[x][y]: x,y 까지 이동했을 때 가져올 수 있는 최대 사탕 개수

dp[0][0]=mp[0][0]
for i in range(1,M):
    #print(f"dp[0][{i}]=dp[0][{i-1}]+mp[0][{i}]")
    dp[0][i]=dp[0][i-1]+mp[0][i]
for i in range(1,N):
    dp[i][0]=dp[i-1][0]+mp[i][0]
#[print(a, end='\n') for a in dp] # 이거 외우기
if N==1 or M==1:
    print(dp[N-1][M-1])
else:
    for i in range(1,N):
        for j in range(1,M):
            dp[i][j]=max(dp[i-1][j]+mp[i][j] ,dp[i][j-1]+mp[i][j])
            #print(f"dp[{i}][{j}]=dp[{i-1}][{j}]+dp[{i}][{j-1}]+mp[{i}][{j}]={dp[i-1][j]}+{dp[i][j-1]}+{mp[i][j]}")
            #[print(a, end='\n') for a in dp]
    print(dp[N-1][M-1])

'''
3 4
1 2 3 4
0 0 0 5
9 8 7 6
'''