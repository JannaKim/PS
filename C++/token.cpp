#include<stdio.h>
#include<string.h>

int main() {

   int N, i = 0;
   char* tok;
   char word[100];
   char str[300] = { 0, };

   scanf("%d", &N);
   rewind(stdin);
   gets(str);
   tok = strtok(str," ");

   while (tok != NULL) {

      word=*tok;
      printf("%s\n", word);
      for(int i=0;word[i];i++){
         printf("%c\n", word[i]);
      }
      tok = strtok(NULL, " ");

   }

   return 0;
}