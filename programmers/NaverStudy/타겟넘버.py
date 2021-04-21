def solution(numbers, target):
    L=[0]+numbers[:]
    # -1000*20~1000*20 = 40000
    n= len(numbers)
    dp= [[0]*(40000+10) for _ in range(n+1)]
    zero=20000
    dp[0][zero]= 1
    
    for i in range(1, 1+n):
        for j in range(40000+10):
            if dp[i-1][j]:
                dp[i][j+L[i]]+=dp[i-1][j]
                dp[i][j-L[i]]+=dp[i-1][j]

    answer = dp[n][zero+target]
    return answer


print(solution(	[1, 1, 1, 1, 1], 3))