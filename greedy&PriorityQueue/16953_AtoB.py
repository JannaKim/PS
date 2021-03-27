a, b= input().split()
ans=-1
def backtrack(x,n):
    global ans
    if x==a:
        ans=n
        return
    if len(x)>1 and x[-1]=='1':
        backtrack(x[:-1],n+1)
    if int(x)%2==0:
        backtrack(str(int(x)//2),n+1)
    
backtrack(b,1)
print(ans)


a, b= map(int, input().split())
cnt=1;
while b>a:
    if b%10==1:
        b//=10
        cnt+=1
    elif not b%2:
        b//=2
        cnt+=1
    else: break
if a==b: print(cnt)
else: print(-1)