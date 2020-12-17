#include<stdio.h>
#include<math.h>

int main()
{
   /*조규현의 좌표 (x1, y1)와 백승환의 좌표 (x2, y2)가 주어지고, 
   조규현이 계산한 류재명과의 거리 r1과 백승환이 계산한 류재명과의 거리 r2가 주어졌을 때,
    류재명이 있을 수 있는 좌표의 수를 출력하는 프로그램을 작성하시오.
    한 줄에 x1, y1, r1, x2, y2, r2가 주어진다.
    
    x1, y1, x2, y2는-10,000보다 크거나 같고, 10,000보다 작거나 같은 정수이고,
   r1, r2는 10,000보다 작거나 같은 자연수이다.*/
   int tc;
   scanf("%d\n",&tc);
   while(tc--)
   {
      int x1,y1,r1,x2,y2,r2;
      scanf("%d %d %d %d %d %d",&x1,&y1,&r1,&x2,&y2,&r2);

      double dis = sqrt( pow(x1-x2,2) + pow(y1-y2,2));
      //if((int)dis != dis) {printf("0\n"); continue;}

      //고정: r1<r2 이도록
      if(r1>r2){
         int temp= r1;
         r1=r2;
         r2=temp;
      }
/*
원이 두 점에서 만나는 경우

r2 - r1 < d < r1 + r2
*/

      // 안
      if(dis<r2){
         if(dis==0&&r1==r2) printf("-1\n");
         else if(r2-r1<dis&&dis<r1+r2) printf("2\n");
         else if(dis+r1==r2) printf("1\n");
         else printf("0\n");
      }

      //밖
      else{
         if(r2-r1<dis&&dis<r1+r2) printf("2\n"); // 이부분 부족한듯
         else if(dis==r1+r2) printf("1\n");
         else printf("0\n");
      }
   }
   
      
      
}