#include <stdio.h>
#include <string>
#include <cstring>
#include <iostream>
using namespace std;
int main()
{
    while(1)
    {

        char curLine[100+1];
        scanf("%[^\n]",curLine); // (scanf는 앞뒤 공백을 무시하므로 한줄 전체를 그대로 받는 데에는 적절치 못하다.)
        
        //char *token = strtok(curLine,'\0');
        
        //string s;
        //getline(cin,s);
        //int lineLen=s.size();

        //const char *curLine = s.c_str();
        if(curLine[0]=='.') break;

        char bracket_sta[100+1];
        int top= -1;
        bool isBalanced= true;
        for(int i=0; curLine[i]; ++i)
        {
            char curChar = curLine[i];
            if(curChar=='(' || curChar=='[') bracket_sta[++top]=curChar;

            else if(curChar==')') 
            {
                if(bracket_sta[top]=='(') --top;
                else
                { 
                    isBalanced=false;
                    break;
                }
            }
            else if(curChar==']') 
            {
                if(bracket_sta[top]=='[') --top;
                else
                { 
                    isBalanced=false;
                    break;
                }
            }
            

        }

        if(isBalanced==false || top!= -1) printf("%s\n","no");
        else if(top==-1) printf("%s\n","yes");

    }
}