# max T 시간 내에 일을 가장 오래 하되 가장 많은 가짓수로 일하는 방법
import math
A = [2,1,4,6,3]
T = 9
#dp= [[0]*(len(A)+1)]+[[0]*len(A)+[math.inf] for _ in range(T)]
dp= [[0]*(len(A)+1) for _ in range(T+1)]
mx=0
for i, time in enumerate(A):
    for j in range(T,-1,-1):
        if dp[j][-1] or j==0:
            if j+time<=T and dp[j+time][-1]<dp[j][-1]+1:
                dp[j+time][-1]=dp[j][-1]+1
                for k in range(len(A)):
                    dp[j+time][k]= dp[j][k]
                dp[j+time][i]=1    
                mx=max(mx,j+time)
print(mx, dp[mx])

A.sort()
s = 0
num=0
for i in range(len(A)):
    s+=A[i]
    num+=1
    if s>T:
        print(num-1)
        break
    

        
