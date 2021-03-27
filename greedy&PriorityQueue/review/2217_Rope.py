n= int(input())
L= [int(input()) for _ in range(n)]
L.sort()
ans=0
for i in range(n):
    ans=max(ans, L[i]*(n-i))
print(ans)