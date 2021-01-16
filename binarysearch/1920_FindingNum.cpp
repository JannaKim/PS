#include <stdio.h>
#include <algorithm>
#include <vector>
#define FOR(i,n) for(int i=0;i<n;++i)
using namespace std;
int main()
{
    int n;
    scanf("%d",&n);
    vector <int> numbers;
    FOR(i,n)
    {
        int x;
        scanf("%d",&x);
        numbers.push_back(x);
    }
    sort(numbers.begin(), numbers.end()); //nlogn
    int m;
    scanf("%d",&m);
    while(m--)
    {
        int x;
        scanf("%d",&x);
        int a=0;
        int b=n-1;
        int m;
        while(a<b)
        {
            m= (a+b)>>1;
            if(numbers[m]<x) a=m+1;
            else b=m;
        }
        if(numbers[a]==x) printf("1\n");
        else printf("0\n");
    }
}