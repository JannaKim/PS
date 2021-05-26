from bisect import bisect_right as bs
n= int(input())
dp=[1e9]*(n+1)
dp[0]=-1
L=[*map(int, input().split())]
for el in L:
    ths= bs(dp,el)
    if dp[ths-1]<el:
        dp[ths]=el
#print(dp)
for i in range(n,0,-1):
    if dp[i]<1e9:
        print(i)
        break