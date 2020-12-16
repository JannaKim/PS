#include<stdio.h>
#include<string.h>
#include<cstring>
#include<iostream>

int main() {

   int N, i = 0;
   char* tok;
   char *num[100] = { 0, };
   char str[300] = { 0, };

   scanf("%d", &N);
   rewind(stdin);
   gets(str);
   tok = strtok(str," ");

   while (tok != NULL) {

      num[i]=tok;// 주소를 주는 것이므로 이렇게 줘야함
      tok = strtok(NULL, " ");
      i++;

   }

   for (int k = 0; k < N; k++) {

      
      printf("%s\n", num[k]); //num[k]가리키는 

   }
   
   return 0;
}