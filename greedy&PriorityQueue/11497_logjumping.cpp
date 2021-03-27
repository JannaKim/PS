#include <iostream>
#include <vector>
#include <algorithm>
#include<stdio.h>
using namespace std;
#define FOR(i,n) for(int i=1;i<n;++i)
int main()
{
    int tc;
    scanf("%d\n",&tc);
    while(tc--)
    {
        int n;
        vector<int> log;
        scanf("%d\n",&n);
        for(int i=0;i<n;++i)
        {
            int x;
            scanf("%d",&x);
            log.push_back(x);
        }
        sort(log.begin(),log.end(), greater<int>());
        vector<int> seq;
        int left=log[0];
        int right=log[0];
        int mx=0;
        FOR(i,n){
            if(i%2==1){
                mx= max(left-log[i], mx);
                left=log[i];
            }
            else{
                mx= max(right-log[i], mx);
                right=log[i];
            }
        }
        printf("%d\n", mx);
        
    }
}




//max(|e - b,c,d| ) 두개 가져오기

