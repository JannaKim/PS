#include <vector>
#include <stdio.h>
#include <algorithm>
using namespace std;

vector<int> edge[1000000+1];
int dp[1000000+1][2];

void topdown(int v,int v1){
    dp[v][0] = 0;
    dp[v][1] = 1;
    for(auto v2: edge[v]){
        if(v2 == v1)
            continue;
        topdown(v2,v);
        dp[v][0]+= dp[v2][1];
        dp[v][1]+= min(dp[v2][0], dp[v2][1]);
    }
}
int main(){
    int n;
    scanf("%d", &n);
    for(int i=0; i<n-1;i++)
    {
        int a, b;
        scanf("%d %d", &a, &b);
        edge[a].push_back(b);
        edge[b].push_back(a);
    }

    topdown(1, 0);

    printf("%d",min(dp[1][0], dp[1][1]));
    return 0;
}