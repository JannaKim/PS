#include <iostream>
#include <vector>
#include <queue>
using namespace std;


void putCabbages(vector<vector <bool>>& field);

void bfs(int y, int x, vector<vector <bool>>& field, vector<vector <bool>>& vis);

bool bound(int y, int x);

int tc, ans;
int row, col, cabbages; // global?
int dy[] = {0, 0, 1, -1};
int dx[] = {1, -1, 0, 0}; // !

int main(){
    cin >> tc;
    while(tc--){
        cin >> col >> row >> cabbages;
        vector < vector <bool> > field(50,vector <bool>(50,false)); // declare + init
        vector < vector <bool> > vis(50,vector <bool>(50,false)); // declare + init
        putCabbages(field);

        ans = 0;
        for(int i = 0; i < row; ++i){
            for(int j = 0; j < col; ++j){
                if(field[i][j] && !vis[i][j]){
                    ++ans;
                    bfs(i, j, field, vis);
                }
            }
        }
        cout << ans << "\n";
    }

}

void putCabbages(vector<vector <bool>>& field){
    while(cabbages--){
        int r, c;
        cin >> c >> r;
        field[r][c] = true;
    }
}

void bfs(int y, int x, vector<vector <bool>>& field, vector<vector <bool>>& vis){
    vis[y][x] = true;
    queue< pair<int, int> > q;
    q.push({y, x});
    while(!q.empty()){
        int cy = q.front().first;
        int cx = q.front().second;
       
        q.pop();

        for(int i = 0; i < 4; ++i){
            int ny = cy + dy[i];
            int nx = cx + dx[i];
            if(bound(ny, nx) && !vis[ny][nx] && field[ny][nx]){
                vis[ny][nx] = true;
                q.push(make_pair(ny, nx));
            }
        }


    }

}

bool bound(int r, int c){
    if(r < 0 || r >= row) return false;
    if(c < 0 || c >= col) return false;
    return true;
}