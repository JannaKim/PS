'''
import math

N = int(input())
dp=[0,1]
for i in range(2,N+1):
    if math.sqrt(i) == float(int(math.sqrt(i))):# 제곱수라면
        dp.append(1)
    else:
        dp.append(i)
    for j in range(1,i//2+1):
        #print(f"dp[{i}] = max(dp[{j}]+dp[{i-j}], dp[{i}])")
        dp[i] = min(dp[j]+dp[i-j], dp[i])
    #print(f"dp[{i}]={dp[i]}")
print(dp[N])

'''
import sys

N = int(sys.stdin.readline())

d = [i for i in range(N+1)]

'''
for i in range(1, N+1):    
    d[i] = min([d[i-j*j]+1 for j in range(1, int(i**0.5)+1)])
'''

for i in range(1, N+1):    
    for j in range(1, int(i**0.5)+1):
        if d[i-j*j]+1 < d[i]:
            d[i] = d[i-j*j]+1
            print(f"d[{i}] = d[{i}-{j}*{j}]+1")   

print(d[N])

