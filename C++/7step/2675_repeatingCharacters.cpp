#include <string>
#include <string.h>
#include <iostream>
#include <stdlib.h>
using namespace std;

int main()
{
    int nmOftc;
    scanf("%d\n",&nmOftc);
    while(nmOftc--)
    {

        char Line[2+10+1];
        scanf("%[^\n]",Line); //getline with char
        char *token = strtok(Line," ");
        int nmOfRep = atoi(token);
        char *word = strtok(NULL," ");

        for(int i=0; word[i]; ++i) //'\0' 전까지 도는 for문
        {
            string cpythswordntimes(nmOfRep,word[i]);
            printf("%s",cpythswordntimes.c_str());
        }
        printf("\n");
    }

}