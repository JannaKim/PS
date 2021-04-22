N, K = map(int, input().split())
L = [[1]*i for i in range(1,N+2)]

for i in range(2,N+1):
    for j in range(1,i):
        L[i][j]=L[i-1][j-1]+L[i-1][j]

print(L[N][K])
