#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int dp[10010];
struct info{
    int v2, cost;
};
vector< vector<info> > edge;
int n, d;

int dijikstra();

int main(){

    fill(&dp[0], &dp[10010], 1e9);
    cin >> n >> d;

    for(int i = 0; i <= d; ++i)
        dp[i]=i;

    for(int i = 0; i < 10010; ++i){
        vector<info> tmp;
        edge.push_back(tmp);
    }

    for(int i = 0; i < n; ++i){
        int v, v2, cst;
        cin >> v >> v2 >> cst;
        if(v2 - v <= cst) continue;
        info cur;
        cur.v2 = v2;
        cur.cost = cst;
        edge[v].push_back(cur);
    }

    int ans;

    for(int i = 0; i < d; ++i){
        if(i) dp[i] = min(dp[i], dp[i - 1] + 1);
        for(auto it : edge[i]){
            dp[it.v2] = min(dp[it.v2], dp[i] + it.cost);
            if(it.v2 > d) continue;
            dp[d] = min(dp[d], dp[it.v2] + d - it.v2);
        }
    }
    cout << dp[d];
}

