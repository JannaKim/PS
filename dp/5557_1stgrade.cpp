#include <stdio.h>
#include <vector>
using namespace std;
#define FOR(i,n) for(int i=1;i<n;++i)
int n;
unsigned long dp_plus[21];
unsigned long dp_minus[21];
unsigned long dp_total[21];
int arr[100+1];
int main()
{
    scanf("%d",&n);
    FOR(i,n+1) scanf("%d",&arr[i-1]);
    
    dp_total[arr[0]]=1;
    FOR(i,n-1){
        for(int j=0;j<21;++j){ // operate: minus
            if(dp_total[j]!=0){
                if(j-arr[i]>=0){
                    dp_minus[j-arr[i]]=dp_total[j];
                }
            }
        }
        for(int j=20;j>=0;--j){ // operate: plus
            if(dp_total[j]!=0){
                if(j+arr[i]<=20){
                    dp_plus[j+arr[i]]=dp_total[j];
                }
            }
        }
        
        for(int j=0;j<=21;++j){ //sum
            if(dp_plus[j]!=0 && dp_minus[j]==0) dp_total[j]=dp_plus[j];
            else if (dp_plus[j]==0 && dp_minus[j]!=0) dp_total[j]=dp_minus[j];
            else if (dp_plus[j]!=0 && dp_minus[j]!=0) dp_total[j]=dp_minus[j]+dp_plus[j];
            else dp_total[j]=0; // init
            dp_plus[j]=0;
            dp_minus[j]=0;
            
        }
        //for(int i=0;i<=20;++i) printf("%d ",dp_total[i]);
        //printf("\n");
    }
    printf("%ld",dp_total[arr[n-1]]);
}