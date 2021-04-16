n, k= map(int, input().split())

a= n//2
if n%2:
    a+=1
b= n-a
if a*b<k:
    print(-1)
    exit()
As= list(range(a))
last=n-1
cur=a-1
curloc= a-1
pair=a*b
while pair>k:
    cur+=1
    As[curloc]=cur
    if cur==last:
        last-=1
        curloc-=1
        cur=As[curloc]
    pair-=1
ans=['B']*n
for el in As:
    ans[el]='A' 
print(''.join(ans))

