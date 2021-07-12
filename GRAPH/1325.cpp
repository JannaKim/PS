#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <vector>
#define maxNode 10000
using namespace std;
int n, m;
vector < vector <int>> edge;
bool vis[maxNode + 1];
void iniEdge(){
    for(int i = 0; i < n + 1; ++i){
    vector<int> tmp;
    edge.push_back(tmp);
}
}

void input(){
    scanf("%d %d", &n, &m);
    iniEdge();
    fill(&vis[0], &vis[maxNode + 1], false);
    for(int i = 0; i < m; ++i){
        int a, b;
        scanf("%d %d", &a, &b);
        edge[b].push_back(a);
    }
    
}


void print(vector<int> &v){
    for(auto it: v) cout << it<<" ";
}

int dfs(int v){
    int cnt = 1;
    for(auto v2: edge[v]){
        if(vis[v2] == false){
            vis[v2] = true;
            cnt += dfs(v2);
        }
    }
    return cnt;
}

void find(vector<int> &ans){
    int mx = -1;
    for(int i = 1; i <= n; ++i){
        fill(&vis[0], &vis[n + 1], false);
        vis[i] = true;
        int cur = dfs(i);
        //cout<<cur<<'\n';
        if(cur> mx){
            mx = cur;
            ans.clear();
            ans.push_back(i);
        }
        else if(cur== mx) ans.push_back(i);

    }
}
int main(){
    
    input();
    vector <int> ans;
    find(ans);
    print(ans);

}