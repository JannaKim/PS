#include <stdio.h>
#include <algorithm>
#include <stdlib.h>
using namespace std;
int main()
{
    int n;
    scanf("%d\n",&n);
    int seq[2000+1]={0,};
    for(int i=0;i<n;i++)
        scanf("%d",&seq[i]);

    int** dp= new int*[2001];
    for(int i=0;i<2001;i++)
    {
        dp[i]= new int[2001];
    }
    
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<n-i;j++)
        {
            if(seq[j]==seq[j+i])
            { 
                dp[j][j+i]=1;
                if(j+1<=j+i-1)
                    {
                        if(dp[j+1][j+i-1]==1) dp[j][j+i]=1;
                        else dp[j][j+i]=0;
                    }
            }
        }
    }    
    int m, a, b;
    scanf("%d",&m);
    for(int i=0;i<m;i++)
    {
        scanf("%d %d",&a,&b);
        printf("%d\n",dp[a-1][b-1]);
    }
    
}