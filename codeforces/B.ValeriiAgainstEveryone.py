t = int(input())
for _ in range(t):
    n = int(input())
    b = [int(i) for i in input().split()]
    a = [2**i for i in b]
    #dp[i][0]: i번째로 끝나는 모든 수열의 합들
    #dp[i][1]: i번째로 시작하는 모든 수열의 합들
    
    dp=[[[] for __ in range(2)] for _ in range(n)]

    for i in range(n):# 시간복잡도 (n^2)/2 + a
        for j in range(i+1):
            S=0
            for k in range(j,i+1):
                S+=a[k]
            dp[i][0].append(S)
        for j in range(i,n):
            S=0
            for k in range(i,j+1):
                S+=a[k]
            dp[i][1].append(S)
    
    yes=False
    L = list(range(n))
    for i in range(n): # 시간복잡도 (n^2)/2
        for j in range(i+1,n):
            if len(set(dp[i][0]+dp[j][1]))<len(dp[i][0]+dp[j][1]):#중복되는게있다
                yes=True
                break
    if yes:
        print("YES")
    else:
        print("NO")
    
'''
2
6
4 3 0 1 2 0
2
2 5
'''

