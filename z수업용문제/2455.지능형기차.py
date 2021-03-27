s=0
ans=-1
for _ in range(4):
    a, b=map(int, input().split())
    s=s-a+b
    ans=max(ans,s)
print(ans)
