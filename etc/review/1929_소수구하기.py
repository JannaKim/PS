from math import*
M, N = map(int, input().split())
Sieve=[0, 0, 1, 1]+[1]*(N+1)
for i in range(2,N//2+1):
    for j in range(2*i,N+1,i):
        Sieve[j]=0
[print(i) for i in range(M,N+1) if Sieve[i]==1]
