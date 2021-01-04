#include <iostream>
#include <vector>
#include <algorithm>
#include<stdio.h>
using namespace std;

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
        sort(log.begin(),log.end());

        
    }
}




//max(|e - b,c,d| ) 두개 가져오기

