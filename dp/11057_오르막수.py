# dp[i][a]: 길이가 i이고 끝자리가 a인 오르막 수의 경우의 수
# print(dp[N])

dp=[0,[1]*10]
#print(dp)

N = int(input())
for i in range(2,N+1): # 자리수만큼 돌림
    dp.append([0]*10) # dp[i].append 할 수 있게 dp[i]?(x) dp[i][]+=해주는거라 안됨
    for a in range(10): #이번 끝자리가 a이고
        for j in range(10): #이전 끝자리가 j일 때
            if j > a: # 내리막
                pass
            else:
                #print(f"이전 끝자리 {j} <= {a}")
                dp[i][a]+=dp[i-1][j]
                #print(dp)

        

print(sum(dp[N])%10007)
