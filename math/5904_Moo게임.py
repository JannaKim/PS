n= int(input())

dp=[]
dp.append(0)
dp.append(3)
i=1
while(2*dp[i]+i+3<=n):
    dp.append(2*dp[i]+i+3)
    i+=1
k=n
idx= i # dp[i]<=k
while True:
    if k>dp[idx]+idx+3:
        k-=(dp[idx]+idx+3) # 얼마나 큰지 모름
    
    elif dp[idx]<k and k<= dp[idx]+idx+3:
        if k==dp[idx]+1:
            print('m')
        else:
            print('o')
        break
    elif k<=dp[idx]:
        idx-=1


