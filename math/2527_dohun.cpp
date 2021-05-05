#include <stdio.h>
#include <math.h>

void distant(int a[4], int b[4]) {
   float ahor = 0, aver = 0, bhor = 0, bver = 0, axmid = 0, aymid = 0, bxmid = 0, bymid = 0;

   ahor = fabs(a[0] - a[2]) / 2;
   aver = fabs(a[1] - a[3]) / 2;
   bhor = fabs(b[0] - b[2]) / 2;
   bver = fabs(b[1] - b[3]) / 2;

   axmid = float(a[0] + a[2]) / 2;
   aymid = float(a[1] + a[3]) / 2;
   bxmid = float(b[0] + b[2]) / 2;
   bymid = float(b[1] + b[3]) / 2;

   float as = fabs(aymid - bymid);
   float bs = fabs(axmid - bxmid);
    printf("%f %f\n", ahor, aymid);
   if (as < (aver + bver) && bs < (ahor + bhor))
   {
      printf("a\n");
   }
   else if(as == (aver + bver) && bs == (ahor + bhor))
   {
      printf("c\n");
   }
   else if (as == (aver + bver) || bs == (ahor + bhor))
   {
      printf("b\n");
   }
   else 
   {
      printf("d\n");
   }
   return;
}
int main() {
   int a[4][4] = { 0, };
   int b[4][4] = { 0, };
   for (int j = 0; j < 4; j++) {
      for (int i = 0; i < 4; i++)
      {
         scanf("%d", &a[j][i]);
      }
      for (int i = 0; i < 4; i++)
      {
         scanf("%d", &b[j][i]);
      }
   }
   for (int j = 0; j < 4; j++) {
      distant(a[j], b[j]);
   }
}