#include <stdio.h>
int n;
int dp[1000+1][2];
int main()
{
    scanf("%d",&n);
    dp[1][0]=1;
    dp[2][1]=1;
    dp[2][0]=1;
    for(int i=3;i<=n;++i)
    {
        dp[i][0]= (dp[i-1][0]+dp[i-1][1])%10007;
        dp[i][1]= (dp[i-2][0]+dp[i-2][1])%10007;  
    }
    printf("%d",(dp[n][0]+dp[n][1])%10007);
}