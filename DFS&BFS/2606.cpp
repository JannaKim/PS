#include <stdio.h>
#include <iostream>

using namespace std;

int par[110] = {0, };

int find(int v){
    if(par[v] == v) return v;
    par[v] = find(par[v]);
    return par[v];
}

void uni(int u, int v){
    int r1 = find(u);
    int r2 = find(v);
    if(r2 < r1){
        int tmp = r1;
        r1 = r2;
        r2 = tmp;
    }
    par[r2] = r1;
}
int main(){
    int n;
    scanf("%d", &n);
    for(int i = 1; i <= n; ++i){
        par[i] = i; // par init
    }
    int m;
    scanf("%d", &m);
    for(int i = 0; i < m; ++i){
        int v, v2;
        scanf("%d %d", &v, &v2);
        uni(v, v2);
    }
    int ans = 0;
    for(int i = 2; i <= n; ++i){
        if(find(i) == 1) ++ans;
    }
    printf("%d", ans);

}