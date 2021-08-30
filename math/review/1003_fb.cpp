#include <iostream>

using namespace std;

// int dp[45][2] = {{1, 0}, {0, 1},};
int dp[45] = {0, 1, 1};
int main(){
    for(int i = 3; i <= 40; ++i){
        dp[i] = dp[i-1] + dp[i - 2];
        // dp[i][0] = dp[i-1][0] + dp[i-2][0];
        // dp[i][1] = dp[i-1][1]+ dp[i-2][1];
    }
    int t;
    cin >> t;
    int n;
    for(int i = 0; i < t; ++i){
        cin >> n;
        if(n == 0) cout << "1 0" << '\n'; // ?
        else cout << dp[n - 1]<<' '<<dp[n]<<'\n';
    }
}