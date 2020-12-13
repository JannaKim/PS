#include <stdio.h>
int main()
{
    
    int tc;
    scanf("%d\n",&tc);
    while(tc--)
    {
        int h, w, n;
        scanf("%d %d %d", &h, &w, &n);
        int floor  = (n-1)%h+1;
        int room = (n-1)/h+1;
        if(room<10)
            printf("%d0%d\n",floor,room);
        else printf("%d%d\n",floor,room);

    }
}
    
/*
   int a;
   scanf("%d\n",&a);
   int x, y, z;
   scanf("%d %d %d\n",&x, &y, &z);
   printf("ㅇㅇ");
   */
