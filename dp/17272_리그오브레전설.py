from time import*
start=time()
N, M = map(int, input().split())


# dp[i]: i초의 조합 가지수: dp[i]= dp[i-1]+dp[i-M]
# int(1e9)+7로 나누기

# 크기: (N+1)-(N-M+2)+1 = M
# M*M 행렬

def mul(n):
    if n==0:
        mp = [[0]*M for _ in range(M)]
        for i in range(M):
            mp[i][i]=1
        [print(i) for i in mp]
        return mp









dp=[0]*(N+1)
dp[1+M] = 2

print(dp)
elif N<M:
    print(1)
else:
    print(mul(N-1)[0][0]%(int(1e9)+7))

print("time :",time()-start)

'''
100000000000000000 100
'''

'''
N = 4
M = 2