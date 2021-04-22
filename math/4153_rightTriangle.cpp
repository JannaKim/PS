#include <stdio.h>
#include <iostream>
#include <algorithm>
using namespace std;
int main()
{
    while(1)
    {
        int a[3+1];
        scanf("%d %d %d",&a[0], &a[1], &a[2]);
        if(a[0]==0&&a[1]==0&&a[2]==0) return 0;
        sort(a,a+3);
        if(a[0]*a[0]+a[1]*a[1]== a[2]*a[2]) printf("right\n");
        else printf("wrong\n");
        
    }
}