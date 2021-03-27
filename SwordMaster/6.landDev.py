from math import log
n= int(input())
L= [*map(int, input().split())]

# dp[i][j]: 땅 i~j를 개발했을 때 얻는 총 이익

dp= [[0]*n for _ in range(n)]

for i in range(n):
    dp[i][i]=L[i]


for i in range(1,int(log(n,2))+1): #간격 만들고
    gap= 2**i
    for j in range(0, n, gap): # 받은 간격별로 채우는데 전간격의 최대값가져간다.
        half= gap//2
        if gap==2:
            dp[j][j+gap-1]= max(dp[j][j],dp[j+1][j+1])
            continue       
        left= dp[j][j+half-1]+max(L[j+half:j+gap])
        right= dp[j+gap//2][j+gap-1]+ max(L[j:j+gap//2])
        dp[j][j+gap-1]= max(left,right)

print(dp[0][n-1])