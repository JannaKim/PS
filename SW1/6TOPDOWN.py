n= int(input())
L= [*map(int, input().split())]


dp= [[0]*n for _ in range(n)]

for i in range(n):
    dp[i][i]=L[i]

def topdown(lo, hi):
    if lo+1==hi:
        dp[lo][hi]= max(L[lo],L[hi])
        return dp[lo][hi]
    if dp[lo][hi]:
        return dp[lo][hi]

    mid= (lo+hi)//2
    left= topdown(lo, mid)
    right= topdown(mid+1,hi)
    if left>right:
        dp[lo][hi]= left+ max(L[mid+1:hi+1])
    else:
        dp[lo][hi]= max(L[lo:mid+1])+ right
    return dp[lo][hi]

print(topdown(0,n-1))