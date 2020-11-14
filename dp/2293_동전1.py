# dp[i] :i 원을 만드는 경우의 수
n,k = [int(i) for i in input().split()]
L=[]
for i in range(n):
    L.append(int(input()))
# 1 2 5
dp=[1]+[0]*k
for won in L: # 이해못했음
    for j in range(won,k+1): 
        dp[j]+=dp[j-won] # 반드시 won을 1번 이상 사용하고 won보다 작거나 같은 동전들로 j원을 만드는 경우의 수
        #print(dp[j-won],"=",dp[j])
        print(f'dp[{j}]={dp[j]}')
        
        

print(dp[k])

#https://www.acmicpc.net/problem/2293
    











