#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    int n;
    scanf("%d",&n);

    int mn = 1000000+1;
    int mx = -1000000-1;
    for(int i=0;i<n;i++)
    {
        int x;
        scanf("%d", &x);
        mn = min(mn, x);
        mx = max(mx, x);
    }

    printf("%d %d",mn, mx);
}