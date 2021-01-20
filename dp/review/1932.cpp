#include <stdio.h>
#include <algorithm>
using namespace std;
#define FOR(i,n) for(int i=1;i<=n;++i)
int dp[500+10][2];


int main()
{
    int n;
    scanf("%d",&n);
    FOR(i,n){
        int tmp;
        FOR(j,i){
            scanf("%d",&tmp);
            dp[j][i%2]= max(dp[j-1][(i-1)%2]+ tmp, dp[j][(i-1)%2]+ tmp);
        }
    }
    int mx=0;
    FOR(i,n) mx=max(mx,dp[i][n%2]);
    printf("%d",mx);

}

/*
#include <iostream>
#include <algorithm>
#define MAX 501
using namespace std;


int main() {
    cin.tie(nullptr);
	cout.tie(nullptr);
    ios::sync_with_stdio(false);
    
    int table[MAX] {};
    int N, n;
    
    cin >> N;
    
    for (int i = 1; i <= N; ++i) {
        for (int j = i; j >= 1; --j) {
            cin >> n;
            table[j] = max(n + table[j-1], n + table[j]);
        }
    }
    
    cout << *max_element(table + 1, table + N + 1);
    
    return 0;
}


*/