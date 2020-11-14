N = int(input())
# 창영 돌 1개 - > 상근 돌 1개
# 창영 돌 1개 - > 상근 돌 3개
# 창영 돌 3개 - > 상근 돌 1개
# 창영 돌 3개 - > 상근 돌 3개

# 상근 돌 1개 - > 창영 돌 1개
# 상근 돌 1개 - > 창영 돌 3개
# 상근 돌 3개 - > 창영 돌 1개
# 상근 돌 3개 - > 창영 돌 3개

'''
dp = [[],[1,3,1,3]]


for i in range(2,N+1):
    dp.append([dp[i-1][0]+1, dp[i-1][1]+3,dp[i-1][2]+1,dp[i-1][3]+3])
    if dp[-1][0]>=N and dp[-1][1]>=N and dp[-1][2]>=N and dp[-1][3]>=N:
        break

if len(dp)%2:
    print('CY')
else:
    print('SK')
'''
N = int(input())
a, b, c, d = 1, 3, 1, 3
i = 1
while a<N or b<N or c<N or d<N:
    i+=1
    a, b, c, d = a+1, b+3, c+1, d+3
    
if i%2:
    print('SK')
else:
    print('CY')
