#include <iostream>
#include <string>
#include <stdio.h>
#include <queue>
#include <vector>
#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
using namespace std;

int money[2]= {2, 5};
int dp[100000+10];
int main(){
    int n;
    scanf("%d", &n);
    
    fill(dp, dp+100001, (int)1e9);
    dp[2] = 1;
    dp[5] = 1;
    for(auto won: money){
        for(int i=1; i<n; ++i){
            if( dp[i] != 1e9 && i + won <= n){
                dp[i + won] = min(dp[i] + 1, dp[i + won]);
            }
        }
    }

    int result = (dp[n] != 1e9) ? dp[n] : -1;
    cout<<result;
    
}