#include <string>
#include <stdio.h>
#include <string.h>
using namespace std;
int main(){
    int tc;
    scanf("%d\n",&tc);
    while(tc--)
    {
        int cnt;
        char word[2+20+1];
        //scanf("%d %[^\n]\n",&cnt, word);
        scanf("%d %s",&cnt, word);

        int wordL=strlen(word);
        for(int i=0;i<wordL;i++)
        {
            for(int j=0;j<cnt;j++)
            {
                printf("%c",word[i]);
            }
        }
        printf("\n");

    }
}