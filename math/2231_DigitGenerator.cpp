#include <iostream>
#include <stdio.h>
#include <cstring>
using namespace std;

int main(){
    int N;
    cin>>N;
    char len[10];
    sprintf(len,"%d",N);
    int digit = strlen(len);

    int begin = N-9*digit;
    char s[10];
    int sum=0;
    bool found = false;
    for(int i=begin; i<N; i++)
    {
        sprintf(s,"%d",i);
        sum=i;
        for(int j=0;j<strlen(s);j++) sum +=s[j]-'0';

        if(sum==N){
            found=true;
            cout<<i<<"\n";
            break;
        }
    }
    if(found==false) cout<<"0\n";
    return 0;
}