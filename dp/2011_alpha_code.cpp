#include <stdio.h>
#include <string.h>
#include <string>
#include <iostream>
using namespace std;
int main()
{
    string s;
    getline(cin,s);

    int* dp= new int[5000+10]; 
    memset(dp, -1, sizeof(int)*5010);
    char* ch;
    ch= (char*)s.c_str();
    if(ch[0]-'0'==0)
    {
        printf("0"); return 0;
    }
    else dp[0]=1;
    if(!ch[1])
    {
        printf("1"); return 0;
    }

    dp[1]= ( (((ch[0]-'0')*10+ (ch[1]-'0')>=10)&&((ch[0]-'0')*10+ (ch[1]-'0')<=26))?1:0 )+ ((ch[1]-'0'>0)?1:0);
    int i=2;
    for(i=2; ch[i];++i)
    {
        dp[i]=( (((ch[i-1]-'0')*10+ (ch[i]-'0')>=10)&&((ch[i-1]-'0')*10+ (ch[i]-'0')<=26))?dp[i-2]:0 )+ ((ch[i]-'0'>0)?dp[i-1]:0);
        dp[i]%=1000000;
        if(dp[i]==0){
            printf("0");
            return 0;
        }
    }
    printf("%d",dp[i-1]%1000000);

}