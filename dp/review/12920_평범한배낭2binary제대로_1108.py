N, M = map(int, input().split())

vc=[]

def binary_pack(v, c, k): # 무게, 만족도, 개수
    a = len(bin(k)[2:]) # 7= 111
    if k == (2**a)-1:
        for i in range(a):
            vc.append((v*(2**i), c*(2**i)))
    else:
        for i in range(a-1): # 5 = 101 = 11 + 10
            vc.append((v*(2**i), c*(2**i)))
        k -= 2**(a-1)-1
        b = bin(k)[2:]
        for digit, bn in enumerate(b[::-1]):
            vc.append((int(bn)*(2**(digit))*v,int(bn)*(2**(digit))*c))

for _ in range(N):
    a, b, c = map(int,input().split())
    binary_pack(a, b, c)


dp = []

# vc: 무게, 만족도
for _ in range(len(vc)):
    dp.append([0]*(M+1))

for i in range(len(vc)):
    for j in range(1,M+1):
        if vc[i][0]<=j:
            dp[i][j] = max(dp[i-1][j-vc[i][0]]+vc[i][1], dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[-1][-1])

'''
3 9
8 5 1
1 2 2
9 4 1
'''

'''
https://www.acmicpc.net/source/20451735
'''