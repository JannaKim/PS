#include <iostream>
#include <vector>
#include <algorithm>
#include <stdio.h>

using namespace std;

int main()
{
    int tc;
    scanf("%d\n",&tc);
    while(tc--)
    {
        int n;
        scanf("%d\n",&n);
        vector<pair<int, int>> candi;
        for(int i=0;i<n;++i)
        {
            int a, b;
            scanf("%d %d",&a, &b);
            candi.push_back({a,b});

        }
        sort(candi.begin(), candi.end());
        int highest_rank=100000+1;
        int cnt=0;
        for(auto [one, two]: candi){
            if(two<highest_rank){ 
            highest_rank= two;
            cnt++;
            }
        }
        printf("%d\n",cnt);
    }
}