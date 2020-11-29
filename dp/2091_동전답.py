dp=[[0]*5 for _ in range(10000)]
a=[0,1,5,10,25]

X, *data = [int(i) for i in input().split()]
data.insert(0,0)
#dp[j][1~i]: 동전 i까지 생각해서 j원 만들때 각 동전 쓴 개수
#dp[j][0]: 최대 동전개수
for i in range(1,5):
    print(f'i {i}')
    for j in range(X,-1,-1):
        print(f'j {j}')
        if dp[j][0] or j==0: # j원을 만드는 동전개수가 차 있을때, 0원일때
            for k in range(1,data[i]+1): #현재 동전을 하나~max까지 써본다
                if j+a[i]*k <=X and dp[j][0]+k>dp[j+a[i]*k][0]:
                    # j원이 다른동전들로 채워져 있거나 0원일때
                    dp[j+a[i]*k][0] = dp[j][0]+k
                    for l in range(1,5): # 가져온 정보 넣는데
                        dp[j+a[i]*k][l] = dp[j][l]
                    dp[j+a[i]*k][i] = dp[j][i]+k # 지금 바꾼 동전넣음
                    print(f'dp[{j}+{a[i]}*{k}] = {dp[j+a[i]*k]}')
print(*dp[X][1:5])

'''
12 5 3 1 2
'''