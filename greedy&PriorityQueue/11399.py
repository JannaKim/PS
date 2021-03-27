n= int(input())
L=[*map(int, input().split())]
L.sort()
ans=0
sum=0
for i in range(n):
    sum+=L[i]
    ans+=sum
print(ans)