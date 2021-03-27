#include <stdio.h>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    int n, k;
    scanf("%d %d\n",&n, &k);
    vector<int> coin;
    for(int i=0;i<n;++i)
    {
        int x;
        scanf("%d",&x);
        coin.push_back(x);
    }

    sort(coin.begin(), coin.end(), greater<int>());

    int cnt=0;
    for(auto it: coin)
    {
        if(it<=k)
        {
            cnt+=k/it;
            k%=it;
            
        }
    }
    printf("%d",cnt);

}