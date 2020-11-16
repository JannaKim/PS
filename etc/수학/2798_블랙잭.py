N, M = map(int, input().split())
L = [int(i) for i in input().split()]
mx=0
for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            mx = max(mx, (L[i]+L[j]+L[k] if L[i]+L[j]+L[k]<=M else 0))
print(mx)

'''
10 500
93 181 245 214 315 36 185 138 216 295
'''