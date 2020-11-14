n,k=[int(i) for i in input().split()]
L=[]
for _ in range(n):
    L.append(int(input()))
dp=[0]*(k+1)
for won in L:
    for i in range(won,k+1):
        if i-won==0:
            # dp[0]을 더한다는 것은 현재won만으로 i원을 만드는 경우
            dp[i]+=1
        else:
            dp[i] += dp[i-won] # i원을 만들기 위해 won을 반드시 1번이상 사용하고 
                        # 나머지를 won과 그 이전의 동전들로 채우는 경우의수
print(dp[k])
