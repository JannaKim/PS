#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int n;
bool visit[30][30];
int dy[] = {0, 0, 1, -1};
int dx[] = {1, -1, 0, 0};
vector <string> village;

int dfs(int y, int x);

int main(){
    cin >> n;
    
    fill(&visit[0][0], &visit[29][30], false);
    for(int i = 0; i < n; ++i){
        string line;
        cin >> line;
        village.push_back(line);
    }
    vector <int> ans;
    
    for(int i = 0; i < n; ++i){
        for(int j = 0; j < n; ++j){
            if(village[i][j] == '1' && !visit[i][j]){
                visit[i][j] = true;
                ans.push_back(dfs(i, j));
            }
        }
    }
    sort(ans.begin(), ans.end());
    cout << ans.size() <<'\n';
    for(auto it : ans) cout << it << '\n';

}

bool bound(int y, int x){
    if(y < 0 || y >= n) return false;
    if(x < 0 || x >= n) return false;
    return true;

}
int dfs(int y, int x){
    int cnt = 1;
    int ny, nx;
    for(int i = 0; i < 4; ++i){
        ny = y + dy[i];
        nx = x + dx[i];
        if(bound(ny, nx) && village[ny][nx] == '1' && !visit[ny][nx]){
            visit[ny][nx] = true;
            cnt += dfs(ny, nx);
        }

    }
    return cnt;
}

/*
7
0000111
0100000
0111110
0111000
0110100
0110101
1110101

*/