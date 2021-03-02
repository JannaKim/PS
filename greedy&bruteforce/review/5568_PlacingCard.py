import sys; input= lambda: sys.stdin.readline().rstrip()
n= int(input())
k= int(input())
L=[int(input()) for _ in range(n)]

ans=set()
chk= [False]*(n+1)
def backtrack(cnt, num):
    if cnt==k:
        ans.add(num)
        return
    for i in range(n):
        if not chk[i]:
            chk[i]=True
            if L[i]<10:
                backtrack(cnt+1, num*10+L[i])
            else:
                backtrack(cnt+1, num*100+L[i])
            chk[i]=False

backtrack(0, 0)
print(len(ans))