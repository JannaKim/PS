#include <stdio.h>

void hanoi(int n, int start, int end)
    {
        if(n==1){printf("%d %d\n",start, end); return;}
        int middle = 6- start- end;
        hanoi(n-1,start,middle);
        printf("%d %d\n",start, end);
        hanoi(n-1,middle,end);
    }

int main()
{
    int n;
    int dp[30]= {0,};
    dp[1]=1;
    scanf("%d",&n);
    for(int i=1;i<=n; i++)
    {
        dp[i]= dp[i-1]*2+1;
    }
    printf("%d\n",dp[n]);
    hanoi(n,1,3);
 

}