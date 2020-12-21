#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(){
    char input[15];
    scanf("%s",input);
    char *tok = strtok(input,".");
    printf("%04d",atoi(tok));
    tok = strtok(NULL,".");
    printf(".%02d",atoi(tok));

    tok = strtok(NULL," ");
    printf(".%02d",atoi(tok));
}