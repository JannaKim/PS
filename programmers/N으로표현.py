
def solution(N, number):
    dp=[1e9]*(100000)
    s=0
    for i in range(5):
        s+=N*10**i
        dp[s]=i+1
        print(s,i+1)
    if N!=1:
        s=0
        for i in range(5):
            s+=1*10**i
        dp[s]=2
    print(dp)
    dp[number]=0   
    #for i in range(1)
    
    return [ans, -1][ans==1e9]

print(solution(5,12))