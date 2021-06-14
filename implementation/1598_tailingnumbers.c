#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main()
{
    int a , b;
    scanf("%d %d",&a , &b);
    --a;
    --b;
    int y1 = a/4;
    int x1 = a%4;
    int y2 = b/4;
    int x2 = b%4;
    
    int ans = abs(y1-y2) + abs(x1-x2);
    printf("%d",ans);
}