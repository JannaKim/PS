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
        //char bin_chunk[6+1]="";
        string raw_bin="      ";
        for(int i=6; i>-1; i--)
        {
            mask=1<<i;
            raw_bin[6-i] = input[j]&mask?'1':'0';
        }
        //printf("%s\n",bin_code);
        int dest=0;
        while(raw_bin[dest]!='1') dest++;

        bin_code += string(raw_bin.substr(dest,7-dest));
    }
    cout<<bin_code<<'\n';

    for(int i=0; i<bin_code.length();)
    {
        //printf("cur= %c\n",bin_code[i]);
        int cnt=0;
        if(bin_code[i]=='0'){
            
            while(bin_code[i]=='0'){ cnt++; i++;}
            cout<<string("00 ")<<string(cnt,'0');
        }
        else if(bin_code[i]=='1'){
            while(bin_code[i]=='1') {cnt++; i++;}
            cout<<string("0 ")<<string(cnt,'0');
        }
        if(i!=7) cout<<" ";
    }




    

}