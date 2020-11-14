from time import*
start=time()
N, M = map(int, input().split())
#dp[i][0]: i초의 마지막에 1초 스킬을 썼을 때 조합 가지수
#dp[i][1]: i초의 마지막에 M초 스킬을 썼을 때 조합 가지수
# int(1e9)+7로 나누기
N+=1
dp=[]
dp=[1,0]*(M-1)
dp+=[1, 1]
print(dp)
for i in range(2*M, N+1):
    dp = dp[2:]+[(dp[-2]+dp[-1])%(int(1e9)+7),(dp[0]+dp[1])%(int(1e9)+7)]
    #dp.append([dp[-1][0]+dp[-1][1], dp[-M][0]+dp[-M][1]])

print((dp[-1]+dp[-2])%(int(1e9)+7))
print("time :",time()-start)

'''
100000000000000000 100
'''