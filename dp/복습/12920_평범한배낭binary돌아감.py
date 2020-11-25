from math import *
N, M = map(int, input().split())
VCK = [] # 무게, 만족도, 개수
for _ in range(N):
    VCK.append(tuple(map(int, input().split())))

vck = []
def binary_pack(v, c, k):
    while k:
        n = int(log(k,2)) # log28 = 3
        if k==2**(n+1)-1:
            for i in range(n+1):
                vck.append((v*(2**i),c*(2**i)))
            break
        else:
            for i in range(n):
                vck.append((v*(2**i),c*(2**i)))
            k -= 2**(n)-1

for i in range(N):
    binary_pack(VCK[i][0], VCK[i][1], VCK[i][2])

dp = []
for _ in range(len(vck)):
    dp.append([0]*(M+1))

for i in range(len(vck)):
    for j in range(1,M+1):
        if vck[i][0]<=j:
            dp[i][j]= max(dp[i-1][j], dp[i-1][j-vck[i][0]] + vck[i][1])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[-1][M])


'''
3 9
8 5 1
1 2 2
9 4 1
'''
    

