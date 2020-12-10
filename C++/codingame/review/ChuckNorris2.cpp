#include <string>
#include <stdio.h>
using namespace std;
int main(){
    char input[7+1];
    scanf("%[^\n]",input);
    string bin="";
    for(char ASCII: input){
        int mask;
        string bin_chunk(7," ");
        for(int i=0;i<7;i++)//7개
        {
            mask=1<<(6-i);
            bin_chunk[i] = mask&ASCII?'1':'0';
        }
        bin+=bin_chunk;
    }

    int binL=bin.length();
    for(int i=0; i<binL;)
    {
        int cnt=0;
        if(bin[i]=='0'){
        while(bin[i]=='0'){ i++; cnt++; }
        printf("00 %s",string(cnt,'0').c_str());
        }
        else if(bin[i]=='1'){
        while(bin[i]=='1'){ i++;cnt++; }
        printf("0 %s",string(cnt,'0').c_str());
        }
        if(i!=binL) printf(" ");

    }

}