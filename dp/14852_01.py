n= int(input())
dp= [[0]*2 for _ in range(max(n,2)+1)]

# dp[i][0]: 위 또는 아래 하나만 채워져있을 때
# dp[i][1]: 둘다 채워졌을때

dp[1][0]=2
dp[1][1]=2

dp[2][0]=6
dp[2][1]= max(2,dp[0][0])+ dp[1][1]*2+ max(dp[0][1],1)

r= 1000000007

#dp[i][0]= dp[i-1][0]+ 2*dp[i-2][1]
#dp[i][1]= dp[i-1][1]*2+ dp[i-2][1]+ dp[i-2][0]

for i in range(3,n+1):
    dp[i][0]= (dp[i-1][1]*2 + dp[i-1][0])%r
    dp[i][1]= (dp[i-1][0]+ dp[i-1][1]*2+ dp[i-2][1])%r

print(dp[n][1])


'''
n= int(input())
#dp= [[0]*2 for _ in range(max(n,2)+1)]

# dp[i][0]: 위 또는 아래 하나만 채워져있을 때-> 2*1사용
# dp[i][1]: 둘다 채워졌을때, 위나 아래중 한쪽만 1*1로 채운 경우는 제외

#dp[i][0]= dp[i-1][0]+ 2*dp[i-2][1]
#dp[i][1]= dp[i-1][1]*2+ dp[i-2][1]+ dp[i-2][0]
a= [2,5]
b= [0,2]
if n==1:
    print(2)
    exit()
elif n==2:
    print(7)
    exit()
c=[0,0]
for i in range(3,n+1):
    c[0]= (a[0]+ 2*b[1])%1000000007
    c[1]=(sum(a)*2+ sum(b))%1000000007
    a, b= c[:], a[:]
    #dp[i][0]= dp[i-1][0]+ 2*dp[i-2][1]
    #dp[i][1]= sum(dp[i-1])*2+sum(dp[i-2])

print(sum(c)%1000000007)
'''