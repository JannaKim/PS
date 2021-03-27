import sys; input= lambda: sys.stdin.readline().strip()
n, s= map(int, input().split())
L=[0]+[*map(int, input().split())]

dp=[0]*(n+1)
tmp=0
for i in range(1,n+1):
    tmp+=L[i]
    dp[i]=tmp

def bs(k,line):
    lo=0
    hi=k
    while lo+1<hi:
        m= (lo+hi)//2
        if line-dp[m]<s:
            hi=m-1
        else:
            lo=m
    if line-dp[hi]>=s:
        return hi
    elif line-dp[lo]>=s:
        return lo
    else:
        return -1e9

mn=1e9
for i in range(1,n+1):
    mn= min(i-bs(i-1,dp[i]),mn)

print([mn,0][mn==1e9])




'''
6 9
2 2 3 1 7 8

'''
