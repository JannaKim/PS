#include <stdio.h>
#include <vector>
#include <iostream>
#include <algorithm>
#include <queue>
using namespace std;
vector <vector <int>> edge;
bool vis[1010];
void dfs(int v);
void bfs(int v); //?
int main(){
    int n, m, v;
    scanf("%d %d %d\n", &n, &m, &v);
    
    edge.clear();
    fill(&vis[0], &vis[1010], false);
    for(int i = 0; i <= n + 1; ++i){ // 여기 실수
        vector <int> tmp;
        edge.push_back(tmp);
    }
    for(int i = 0; i < m; ++i){
        int v, v2;
        scanf("%d %d", &v, &v2);
        edge[v].push_back(v2);
        edge[v2].push_back(v); // 양방향이래
    }
    vis[v] = true;
    printf("%d ", v);
    dfs(v);
    printf("\n");
    fill(&vis[0], &vis[1010], false);
    bfs(v);
}

void dfs(int v){
    sort(edge[v].begin(), edge[v].end());
    for(int v2 = 0; v2 < edge[v].size(); ++v2){
        if(vis[edge[v][v2]] == false){
            vis[edge[v][v2]] = true;
            printf("%d ", edge[v][v2]);
            dfs(edge[v][v2]); // 여기 실수 2
        }
    }
}

void bfs(int v){
    int st = v;
    vis[v] = true;
    queue <int> q;
    q.push(st);
    printf("%d ", st);
    while(q.size()!=0){
        int v;
        v = q.front();
        q.pop();
        for(int v2 = 0; v2 < edge[v].size(); ++v2){
            if(vis[edge[v][v2]] == false){
                vis[edge[v][v2]] = true;
                printf("%d ", edge[v][v2]);
                q.push(edge[v][v2]);
            }
        }
    }
}


