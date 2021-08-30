#include <iostream>
#include <algorithm>
using namespace std;

int n, m;
int dp[110][110];
int main(){
    cin >> n >> m;
    fill(&dp[0][0], &dp[109][110], 1e9);
    
    while(m--){
        int a, b;
        cin >> a >> b;
        dp[a][b] = 1;
        dp[b][a] = 1;
    }

    for(int i = 1; i <= n; ++i){
        dp[i][i] = 0;
        for(int j = 1; j <= n; ++j){
            for(int k = 1; k <= n; ++k){
                dp[j][k] = min(dp[j][k], dp[j][i] + dp[i][k]);
            }
        }
    }
    int ans, mn;
    mn = 101;
    for(int i = 1; i <= n; ++i){
        int sm = 0;
        for(int j = 1; j <= n; ++j)
            sm += dp[i][j];
        
        if(sm < mn){
            mn = sm;
            ans = i;
        }
    }
    cout << ans;
}
