N, M = map(int,input().split()) # N개의 편의점에서 잠복한다
C = [int(i) for i in input().split()]
chk=[0]*(M+1)
for i in range(N):
    chk[C[i]]+=1
print(max(chk))
