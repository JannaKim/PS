d= int(input())
M= int(1e9)+7
dp= [[0]*8 for _ in range(d+1)]
dp[0][0]=1
#dp[i][j]: 정과관부터 i초 산책해서 j관에 도착하는 경우의 수
'''
정보 전산 미래 신양 한경 진리 학생 형남
0   1   2   3   4   5   6  7
'''
edge= [[] for _ in range(8)]
L=[(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4), (2, 4), (3, 5), (4, 5), (5, 6), (6, 7), (4, 7)]
for a,b in L:
    edge[a].append(b)
    edge[b].append(a)
    
for i in range(1,d+1):
    for j in range(8):
        if dp[i-1][j]:
            for v2 in edge[j]:
                dp[i][v2]=(dp[i][v2]+dp[i-1][j])%M

print(dp[d][0])