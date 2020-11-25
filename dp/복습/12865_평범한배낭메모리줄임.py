N, K = map(int, input().split())
WV = []
for _ in range(N):
    a, b = map(int, input().split())
    WV.append((a,b))


L = [0]*(K+1)
M = [0]*(K+1)
for i in range(N):
    if not i%2: #짝
        for j in range(1,K+1):
            
            if WV[i][0]<=j:
                M[j] = max(L[j-WV[i][0]]+WV[i][1],L[j])
            else:
                M[j] = L[j]
    else: #홀
        for j in range(1,K+1):
            
            if WV[i][0]<=j:
                L[j] = max(M[j-WV[i][0]]+WV[i][1],M[j])
            else:
                L[j] = M[j]

    
if not (N-1)%2: # N-1이 짝수면
    print(M[K])
else:
    print(L[K])


'''
4 7
6 13
4 8
3 6
5 12
'''

