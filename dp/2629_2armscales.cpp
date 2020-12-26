#include <stdio.h>
#include <vector>
#include <string.h>
#include <iostream>
using namespace std;

int main()
{
    int n;
    cin>>n;

    vector<int> balance_weight;
    while(n--)
    {
        int x;
        cin>>x;
        balance_weight.push_back(x);
    }
    
    int* dp= new int[40001];
    memset(dp,-1,sizeof(int)*40001);
    

    for(auto it: balance_weight) //30
    {
        for(int wei=15000;wei>-1;--wei) //15000
        {
            if(wei>=it)
                if(dp[wei-it]==1 || wei-it==0) {
                    dp[wei]=1;
                    //printf("%d ",wei);
                }
        }
    }
    
    int m;
    cin>>m;

    int marble;
    while(m--) //7
    {
        bool solved= false;
        cin>>marble;
        if(marble>15000) {{printf("N "); continue;}}
        if(dp[marble]==1){printf("Y "); solved= true; continue;}
        for(int i=0;i<=15000;++i)
        {
            if(dp[i]==1 &&dp[i+marble]==1){printf("Y "); solved= true; break;}
        }

        if(solved==false) printf("N ");
        
    }
    
}