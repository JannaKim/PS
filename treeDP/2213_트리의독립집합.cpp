#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int n;
int dp[10001][2]; // [i][0]: 선택 x, [i][1]: 선택 o
int cost[10001];
vector< vector<int> > edge;
bool vis[10001];
vector<int> ans;

void dfs(int n);
void track(int cur, int prev, bool state);

int main(){
    cin >> n;
    edge.resize(n + 1); // !
    for(int i = 1; i <= n; ++i) cin >> cost[i];
    for(int i = 0; i < n - 1; ++i){
        int a, b;
        cin >> a >> b;
        edge[a].push_back(b);
        edge[b].push_back(a);
    }
    vis[1] = true;
    dfs(1);
    int ans1 = dp[1][0];
    int ans2 = dp[1][1];
    ans1 > ans2 ? track(1, -1, 0) : track(1, -1, 1);
    sort(ans.begin(), ans.end());
    cout << max(ans1, ans2) << '\n';
    for(auto it : ans) cout << it << ' ';
}

void dfs(int v){
    dp[v][1] = cost[v];
    for(auto v2 : edge[v]){
        if(vis[v2]) continue;
        vis[v2] = true;
        dfs(v2);
        dp[v][0] += max(dp[v2][0], dp[v2][1]);
        dp[v][1] += dp[v2][0];
    }
}

void track(int v, int v1, bool state){
    if(state){
        ans.push_back(v);
        for(auto v2 : edge[v]){
            if(v2 == v1) continue;
            track(v2, v, 0);
        }
    }
    else{
        for(auto v2 : edge[v]){
            if(v2 == v1) continue;
            if(dp[v2][1] >= dp[v2][0]) track(v2, v, 1);
            else track(v2, v, 0);
        }
    }
}