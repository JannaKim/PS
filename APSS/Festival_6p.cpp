#include <vector>
#include <string>
#include <stdio.h>
#include <algorithm>
#include <iostream>
using namespace std;

int main(){
    int tc;
    scanf("%d\n", &tc);
    while(tc--)
    {
        int nRent, nRecruit;
        scanf("%d %d\n", &nRent, &nRecruit);
        vector<int> cost;
        vector<double> dp(nRent, 101.0);
        for(int i=0; i<nRent;i++){
            int x;
            scanf("%d",&x);
            cost.push_back(x);
        }
        double ans=101;

        for(int i=0; i<nRent;i++){
            int accum=0;
            for(int j=i; j<nRent; j++)
            {
                double gap=j-i+1;
                accum+=cost[j];

                if(gap>=nRecruit)
                    dp[i]= min(dp[i], accum/gap);
            }
            ans=min(ans, dp[i]);
            }

        printf("%.10f\n",ans);
    }

}