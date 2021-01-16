#include <stdio.h>
#include <algorithm>
#include <vector>
using namespace std;
#define FOR(i,n) for(int i=0;i<n;++i)
#define pb push_back 
#define print printf
#define scan scanf
#define ts "%d",
#define v vector

int main()
{
    int n;
    scan(ts &n);
    v <int> numbers;
    FOR(i,n)
    {
        int x;
        scan(ts &x);
        numbers.pb(x);
    }
    sort(numbers.begin(), numbers.end());
    int left;
    int right;

    int m;
    scan(ts &m);
    int a;
    int b;
    while(m--)
    { 
        int x;
        scan(ts &x);
        a=0;
        b=n-1;
        int m;
        while(a<b)
        {
            m=(a+b)>>1;
            if(numbers[m]<x) a=m+1;
            else b=m;
        }
        if( numbers[a]<x) ++a;
        left=a;
        a=0;
        b=n-1;
        while(a<b)
        {
            m=(a+b)>>1;
            if(numbers[m]<=x) a=m+1;
            else b=m;
        }
        if(numbers[a]<=x) ++a;
        right=a;
        print("%d ",right-left);


    }

}