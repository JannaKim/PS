#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>

int main()
{
    int p = 0;
    int posi = 0;
    int nega = 0;
    scanf("%d", &p);
    for (int i = 0; i < p; i++)
    {
        int tmp; //이거
        scanf("%d", &tmp);
        if (tmp == 1)
        {
            posi++;
        }
    }
    nega = p - posi;
    if (posi > nega)
    {
        printf("Junhee is cute!");
    }
    else
    {
        printf("Junhee is not cute!");
    }
    return 0;
}