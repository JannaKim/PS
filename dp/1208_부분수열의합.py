import sys; input= lambda: sys.stdin.readline().rstrip()
n, s= map(int, input().split())
L= [*map(int, input().split())]
L.sort()
M=[]
for i in range(n):
    if L[i]>=0:
        L, M= L[:i], L[i:]
        break

Mx=100000*40*2
dp=[0]*Mx

for el in L:
    for i in range(100000*40+1,100000*40+1+Mx):
        i%=Mx
        if dp[i]:
            dp[(i+el+Mx)%Mx]+=dp[i]
    dp[el]+=1

for el in M:
    for i in range(100000*40,100000*40-Mx,-1):
        i=(i+Mx)%Mx
        if dp[i]:
            dp[(i+el+Mx)%Mx]+=dp[i]
            
    dp[el]+=1

print(dp[(s+Mx)%Mx])