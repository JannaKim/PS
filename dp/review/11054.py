import sys; input= lambda: sys.stdin.readline().rstrip(); r=range
n= int(input())
up= [1]*n
down= [1]*n


L=[*map(int, input().split())]
up[0]=1
for i in r(1,n):
        for j in r(i-1,-1,-1):
            if L[j]<L[i]:
                up[i]=max(up[i],up[j]+1)

down[n-1]=1
for i in r(n-2,-1,-1):
        for j in r(i+1,n):
            if L[j]<L[i]:
                down[i]=max(down[i],down[j]+1)

ans=1
for i in r(n):
    ans=max(ans,up[i]+down[i]-1)



print(ans)