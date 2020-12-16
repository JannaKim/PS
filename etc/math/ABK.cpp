#include <stdio.h>
#include <cstring>
// findk(char charX[]); Q) 근데 이런식으로 알려줄 수 있지 않았나?


//시간복잡도 O(1)
int k;
int findk(char charX[])
{
    if(charX[0]=='-')return 0;
    int sum=0;
    for(int i=0; charX[i]; i++)
    {
        int cnt=0;

        if(i==0&&(charX[i]-'0')<k) continue;   

        if(i==0){
            if(charX[0]-'0'==k){
                for(int j=1; charX[j]; j++)
                    cnt=10*cnt+(charX[j]-'0');
                cnt+=1;
            }
            else{
                cnt=1;
                for(int j=1; charX[j]; j++)
                    cnt*=10;
            }
        }
        else{
            int beforei=0;
            int afteri=0;
            int temp=1;
            for(int j=0; charX[j]; j++){
                if(j<i) beforei=10*beforei+(charX[j]-'0');
                else if(i<j){
                    afteri=10*afteri+(charX[j]-'0');
                    temp*=10;
                }
            }
            if((charX[i]-'0')==k){
                cnt+=afteri;
                cnt+=beforei*temp;
            }
            else if((charX[i]-'0')<k)
                cnt+=beforei*temp;
            else cnt+=(beforei+1)*temp;
        }
        sum+= cnt;
    }
    return sum;
}



int main()
{
    int a, b;
    scanf("%d %d %d",&a, &b, &k); // a, b = 0~100_000_000
    char charA[10];     
    char charB[10];  
    sprintf(charA, "%d", a-1); 
    sprintf(charB, "%d", b); 
    int ansA=findk(charA); //find all k, range [0,a)
    int ansB=findk(charB); //find all k, range [0~b+1)

    int ans= ansB-ansA;
    printf("%d\n",ans);

}

