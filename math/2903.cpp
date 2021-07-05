#include <stdio.h>
#include <math.h>
//long long dp[20] = {0, };
int main(){
    int n;
    scanf("%d", &n);
    /*
    dp[1] = 3;
    for(int i = 2; i< n + 1; ++i){
        dp[i] = 2 * dp[i - 1]- 1;
    }
    printf("%lld\n", (long long)(pow(dp[n], 2)));
    */
 
    printf("%lld", (long long)pow( (long long)pow(2, n)+ 1, 2));
    //
}