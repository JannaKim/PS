import sys; input= lambda: sys.stdin.readline().rstrip()

def coinChange(coins, amount):
    dp= [0]+[1e9]*amount
    for won in coins:
        for i in range(amount+1):
            if (i==0 or dp[i]<1e9) and i+won<=amount:
                dp[i+won]=min(dp[i+won], dp[i]+1)

    return [dp[amount],-1][dp[amount]==1e9]

#print(coinChange([2], 3))