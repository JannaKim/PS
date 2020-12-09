#include <cstring>
#include <string>
#include <stdio.h>
#include <string.h>
#include <iostream>
using namespace std;

int main()
{
    char input[7+1];
    scanf("%[^\n]", input);
    string bin_code="";
    for(int j=0; input[j]; j++)
    {
        int mask;
        string raw_bin="       "; //자릿수 *로 표현?
        for(int i=6; i>-1; i--)
        {
            mask=1<<i;
            raw_bin[6-i] = input[j]&mask?'1':'0';
        }
        /*
        int dest=0;
        while(raw_bin[dest]!='1') dest++;

        bin_code += string(raw_bin.substr(dest));
        */
        bin_code += raw_bin;

    }
    //cout<<bin_code<<'\n';
    int binLen=bin_code.length();

    for(int i=0; i<binLen;)
    {
        int cnt=0;
        if(bin_code[i]=='0'){
            
            while(bin_code[i]=='0'){ cnt++; i++;}
            cout<<string("00 ")<<string(cnt,'0');
        }
        else if(bin_code[i]=='1'){
            while(bin_code[i]=='1') {cnt++; i++;}
            cout<<string("0 ")<<string(cnt,'0');
        }
        if(i!=binLen) cout<<" ";
    }




    

}