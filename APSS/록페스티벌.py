tc = int(input())
for _ in range(tc):
    nRent, nRecruit = tuple(map(int, input().split()))
    cost = [int(i) for i in input().split()]

    dp = [101.0]*nRent

    for i in range(nRent):
        sum=0
        for j in range(i,nRent):
            succesiveD= j-i+1
            sum+=cost[j]
            if succesiveD>=nRecruit:
                dp[i] = min(dp[i], float(sum/succesiveD))
       
    print(f'{min(dp):.10f}')

