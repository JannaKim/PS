#include <stdio.h>
#include <algorithm>
#include <vector>
using namespace std;

int main()
{
    int n;
    scanf("%d",&n);
    vector <int> ropes;
    for(int i=0; i<n; ++i)
    {
        int x;
        scanf("%d",&x);
        ropes.push_back(x);
    }
    sort(ropes.begin(), ropes.end());

    int mx=0;
    for(int i=0; i<n;++i){
        mx= max(mx, ropes[i]*(n-i));
    }
    printf("%d",mx);
}