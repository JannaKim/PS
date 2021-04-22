'''
n, m= map(int, input().split())
dp=[0]*(n+1)
L=[*map(int, input().split())]
dp[0]=0
for i in range(1,n+1):
    dp[i]=dp[i-1]+L[i-1]
ans=0
chk={}
def rec(lo, hi):
    #print(lo,hi)
    if lo>hi:
        return
    global ans, m
    if dp[hi]-dp[lo-1]>m:
        rec(lo+1,hi)
        rec(lo,hi-1)
    elif dp[hi]-dp[lo-1]==m:
        if (hi,lo-1) not in chk:
            chk[(hi,lo-1)]=True
            ans+=1


lt=1
rt=n
rec(lt,rt)
print(ans)
'''

n, m= map(int, input().split())
dp=[0]*(n+1)
L=[*map(int, input().split())]
dp[0]=0
for i in range(1,n+1):
    dp[i]=dp[i-1]+L[i-1]

ans=0
lo=0
for hi in range(1,n+1):
    while dp[hi]-dp[lo]>m:
        lo+=1
    if dp[hi]-dp[lo]==m:
        ans+=1
print(ans)
