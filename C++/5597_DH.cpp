#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>

int main()
{
    int temp = 0;
    int a[30] = { 999, };

    for (int i = 0; i < 30; i++)
    {
        a[i] = 999;
    }
    while (temp < 28)
    {
        scanf("%d", &a[temp]);
        temp++;
    }
    for (int i = 0; i < 29; i++)
    {
        for (int j = i + 1; j < 30; j++)
        {
            if (a[i] > a[j])
            {
                temp = a[i];
                a[i] = a[j];
                a[j] = temp;
            }
        }
    }

    temp = 1;
    for (int i = 1; i <= 30;)
    {
        if (a[i - 1] == temp)
        {
            temp++;
            i++;
        }
        else if (a[i - 1] > 30)
        {
            return 0;
        }
        else if (a[i - 1] != temp)
        {
            printf("%d\n", temp);
            temp++;
        }
    }
    return 0;
}

/*
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
*/