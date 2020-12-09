#include <string>
#include <string.h>
#include <iostream>
#include <stdlib.h>
using namespace std;

int main()
{
    int testcases;
    scanf("%d\n",&testcases);
    for(int i=0;i<testcases;++i)
    {
        //getchar();
        //scanf("%*c");
        /*
        char Line[2+10+1];
        const char *word;

        int cnt;
        if(i!=testcases-1){ 
            scanf("%*c");
            scanf("%[^\n]",Line); //getline with char
            char *token = strtok(Line," ");
            cnt = atoi(token);
            word = strtok(NULL," ");
        }
        else{ 
            scanf("%d",&cnt);
            getchar();
            getline(cin,s,'\n');
            word = s.c_str();
        }
        */
       int cnt;
       scanf("%d ",&cnt);
       string str;
       getline(cin,str,'\n'); // 이 문자 추출시 중단. 스트림에서도 사라짐

        for(int j=0; j<str.length(); j++) //'\0' 전까지 도는 for문
        {
            //string cpythswordntimes(cnt,str[i]);
            //printf("%s",cpythswordntimes.c_str());
            cout<<string(cnt,str[j]);
        }
        printf("\n");
    }

}

/*
10
1 a
2 a
3 a
4 a
5 a
6 a
7 a
8 a
9 a
10 a
*/