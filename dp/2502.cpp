#include <vector>
#include <stdio.h>
using namespace std;
int main(){
    /*
    a b a+b a+2b 2a+3b 3a+5b 5a+8b 8a+13b
    1 2 3    4    5     6     7      8

    */

    int afib[30+1] = {0, 1, 0,};

    int bfib[30+1] = {0, 0, 1,};

    int d,k;
    scanf("%d %d", &d, &k);
    for(int i=3;i<=d;i++)
    {
        afib[i]= afib[i-1]+afib[i-2];
        bfib[i]= bfib[i-1]+bfib[i-2];
    }
    //2차식
    //afib[d]*a + bfib[d]*b= k;
    
    for(int a=1;a<=100000;a++)
    {
        if(k>afib[d]*a && (k-afib[d]*a)%bfib[d] == 0)
        {
            printf("%d\n%d",a, (k-afib[d]*a)/bfib[d]);
            break;
        }
    }

}