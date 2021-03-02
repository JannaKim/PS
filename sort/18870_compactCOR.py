n= int(input())
R=[*map(int, input().split())]
L=[[R[i], i] for i in range(n)]

L.sort()

ans=[0]*n
ans[L[0][1]]=0
rank=0
for a,b in zip(L,L[1:]):
    if a[0]!=b[0]:
        rank+=1
        ans[b[1]]=rank
    else:
        ans[b[1]]=rank

print(*ans)