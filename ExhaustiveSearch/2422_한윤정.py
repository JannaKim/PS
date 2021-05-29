n, m= map(int, input().split())
nots={}
for _ in range(m):
    a,b= map(int,input().split())
    if b<a:
        a,b= b,a
    nots[(a,b)]=True

ans=0
for i in range(1,n-1):
    for j in range(i+1,n):
        for k in range(j+1, n+1):
            if (i,j) in nots:
                continue
            if (j,k) in nots:
                continue
            if (i,k) in nots:
                continue
            ans+=1

print(ans)