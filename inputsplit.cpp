#include <iostream>
#include <sstream>
#include <string>
using namespace std;

/*
int main()
{
    string input;
    getline(cin,input);
    stringstream splt_Input(input);
    cout<<splt_Input<<"\n";
}

*/
#include <cstring>
#include <iostream>
#include <stdio.h>
int main() 
{
    //char* input = "abcd"; // 바로 초기화는 가능
    char input[100000+1];
    scanf("%[^\n]",input);
    cout<<input<<"\n";
    
    char *token = std::strtok(input, " ");
    int cnt=0;
    while (token != NULL) {
        ++cnt;
        cout<<token<<"\n";
        token = std::strtok(NULL, " ");
    }
    cout<<cnt<<"\n";
    
}