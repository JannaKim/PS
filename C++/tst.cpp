#include <stdio.h>

int main()
{
    char hi[256];
    FILE *text= NULL;  
    FILE *kiki= NULL;                       
    text= fopen("test.txt","r");
    kiki= fopen("dudu.txt","r");

    bool flag=true;
    int a=10;
    while(a--)
    {
        if(flag==true)
        {
            fgets(&hi[0],256, text);
            for(int i=0; hi[i]; i++)
                printf("%c",hi[i]);
            flag=false;
            }
        else
        {
            fgets(&hi[0],256, kiki);
            for(int i=0; hi[i]; i++)
                printf("%c",hi[i]);
            flag=true;
        }
    }
}