dp= [0]+[1e9]*125
for won in (1, 10, 25):
    for i in range(100):
        dp[i+won]= min(dp[i]+1, dp[i+won])

t= int(input())
for _ in range(t):
    price= input()
    leng= len(price)
    s=0
    for i in range(leng,0,-2):
        a= max(0, i-2)
        s+=dp[int(price[a:i])]
    print(s)