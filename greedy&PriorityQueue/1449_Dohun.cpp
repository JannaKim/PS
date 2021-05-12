#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <string>

using namespace std;

int arr[1000+1];

int main()
{
   int n = 0, l = 0, temp = 0, cnt = 0, m = 0, gap = 0, a = 0, swi = 0;

   scanf("%d", &n);
   scanf("%d", &l);
   memset(arr, 0, sizeof(int));

   for (int i = 0; i < n; i++)
   {
      scanf("%d", &a);
      arr[a] = 1;
      
   }

   temp = 0;
   for (int i = 1; i <= 2000; i++)
   {
      if (arr[i] == 1 && swi == 0)
      {
         swi = 1;
      }
      if (swi == 1)
      {
         //printf("%d ", i);
         m++;
         if (m == l)
         {
            //printf("---- 추가됨.\n");
            cnt++;
            m = 0;
            swi = 0;
            continue;
         }
      }
   }
   printf("%d", cnt);
}
