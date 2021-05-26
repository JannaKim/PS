n= int(input())
L=[*map(int, input().split())]

ans=0
for i in range(n):
    for j in range(i+1,n):
        if L[j]>L[i]:
            ans=max(ans, j-i4)
            break
print(ans)
