#dp[i]: 숫자 i를 1,2,3 조합으로 나타내는 방법의 수
# 한칸 두칸 세칸

T = int(input())

for _ in range(T):
    dp=[0,1,2,4]
    n = int(input())
    if n<=3:
        print(dp[n])
    else:
        for i in range(4,n+1):
            dp.append(dp[i-1]+dp[i-2]+dp[i-3])

        print(dp[n])

# https://www.acmicpc.net/problem/9095
            
