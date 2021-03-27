#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
int main()
{
   int temp = 0;
   bool a[31]={false,};
   //memset (a, true, sizeof(a));

   while (temp < 28)
   {
        int tmp;
      scanf("%d", &tmp);
      a[tmp]=true;
      temp++;
   }

   for (int i = 1; i <= 30;i++)
       if(a[i]==false) printf("%d\n",i);

   return 0;
}


/*
if (a[i - 1] == temp)
{
    temp++;
    i++;
}
else if (a[i - 1] == 999)
{
    return 0;
}
else if(a[i - 1] != temp)c
{
    printf("%d\n", temp);
    temp++;
}
*/