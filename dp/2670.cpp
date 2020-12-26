#include <stdio.h>
#include <vector>
#include <algorithm>
using namespace std;
int main(){
    vector<double> sequence;
    int n;
    scanf("%d\n",&n);
    for(int i=0;i<n;i++)
    {
        double x;
        scanf("%lf",&x);
        sequence.push_back(x);
    }

    vector<double> dp;
    for(int i=0;i<n;i++) dp.push_back(0);

    dp[0]=sequence[0];
    for(int i=1;i<n;i++)
    {
        dp[i]= max(dp[i-1]*sequence[i], sequence[i]);
    }
    printf("%.3lf",*max_element(dp.begin(),dp.end()));

}

/*
8
1.1
0.7
1.3
0.9
1.4
0.8
0.7
1.4
*/