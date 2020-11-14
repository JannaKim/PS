n , k = [int(i) for i in input().split()]
L=[]
for i in range(n):
    L.append(int(input()))
dp=[0]+ [k*2]*k
for i in range(1,k+1): #  하나의 동전만으로 i원 만들수 있으면 그 개수 일단 집어넣음
    for j in L:
        if not i%j: # 나눠 떨어진다면
            dp[i] = min(dp[i] ,i//j)

#print(dp)

# 어떻게 줄이지?

# dp[i]: i원을 만들 수 있는 동전 최소개수
for i in range(1,k+1):
    for j in range(1,i+1):
        # dp[i=2*j] = dp[j]+dp[j] 중복
        dp[i] = min(dp[j]+dp[i-j],dp[i])

for i in range(len(dp)):
    if dp[i]==2*k:
        dp[i]=-1
        
#print(dp)
print(dp[k])
