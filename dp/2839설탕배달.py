import sys

n= int(input())
'''
dp=[0]+[1e9]*(n+5)
for bag in (5, 3):
    for i in range(n+1):
        if i==0 or dp[i]:
            dp[i+bag]= min(dp[i]+1, dp[i+bag])
print([dp[n],-1][dp[n]==1e9])
'''

five=n//5
while five>=0:
    if (n-five*5)%3==0:
        print(five+(n-five*5)//3)
        sys.exit()
    five-=1
print(-1)
'''

n=int(input())
r=n%5
while r%3!=0:
    r+=5
if(n-r<0):
    print(-1)
else:
    print(r//3+(n-r)//5)
'''
