n,m=map(int,input().split())
j=int(input())
p=[]
for i in range (j):
    q=int(input())
    p.append(q)
left=1
right=left+m-1
ans=0

for i in p:
    if i<left:
        ans+=left-i
        left=i
        right=left+m-1
    elif i>=left and i<=right:
        ans+=0
    elif i>right:
        ans+=(i-right)
        right=i
        left=right-m+1
print(ans)