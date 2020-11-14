N = int(input())
L = []
for _ in range(N):
    a, b = input().split()
    L.append((a, int(b)))

L.sort(key = lambda x:x[1])

mx = L[-1][1]
M = [L[-1][0]]
for i in range(N-2,-1,-1):
    if L[i][1]==mx:
        M.append(L[i][0])

M.sort()

print(M[0])
'''
3
a 10
b 10
d 2
'''