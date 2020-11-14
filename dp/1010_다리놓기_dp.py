T = int(input())

# dp[i][j]: 0~i 지점 중 1<j개 곳에 다리를 놓는 경우의 수
#           = dp[i-1][j-1]+ dp[i-1][j]
dp=[]
dp = [[0]]

for _ in range(T):
    dp=[]
    N, M = [int(i) for i in input().split()] # dp[M][N]
    for i in range(0,M+1):
        dp.append([1]+[0]*(M))
        dp[i][i]=1

    for i in range(1,M+1):
        for j in range(1,N+1):
            #print(f"dp[{i}][{j}]=dp[{i-1}][{j-1}]+dp[{i-1}][{j}]")
            dp[i][j]=dp[i-1][j-1]+dp[i-1][j]
            #print(dp)

    print(dp[M][N])

'''
T=int(input())
dp=[[0]*31 for i in range(31)]

for i in range(1,31):
	dp[1][i]=i

for i in range(2,31):
	for j in range(i,31):
		dp[i][j]=dp[i-1][j-1]+dp[i][j-1]

for t in range(T):
	N,M=map(int,input().split())
	print(dp[N][M])
'''