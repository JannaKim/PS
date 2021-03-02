a, b= input().split()
la= len(a)
lb= len(b)
ans=1e9
for i in range(lb-la+1):
    cnt=0
    for x, y in zip(a, b[i:]):
        if x!=y:
            cnt+=1
    ans= min(ans, cnt)
print(ans)