#include <stdio.h>

int main()
{
    int a, b, k;
    scanf("%d %d %d",&a, &b, &k); // 1~100_000_000
    int kUntilA=0;
    int kUntilB=0;

    // find digit
    int nDigit=0;

    while(b/pow(10,nDigit++)){}

    bool closeToUpper= 0;
    bool closeToLower= 0;
    abs(b-pow(10,nDigit))>abs(b-pow(10,nDigit-1))? ~closeToLower : ~closeToUpper;

    if(closeToLower==1)
    {
     kUntilA+= pow(10, nDigit-2)*(nDigit-1);
     for(int i=pow(10,nDigit-1); i<=b; i++)
     {
        
     }    
    }



    








}

int abs(int num)
{
    if(num<0) return -num;
    return num;
}

int pow(int n,int r){
    int result=1;
    for(int i=0;i<r;i++)
        result*=n;
    return result;
}

int countK(int to)
{
    int digit=0; //현재 계산할 자릿수, 0: 1의자리


    while(b/pow(10,digit))
    {

        ans+=b/pow(10,digit) *  
    }

}