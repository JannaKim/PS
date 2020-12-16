#include <stdio.h>
#include <cstring>
// findk(char charX[]); Q) 이런식으로 알려줄 수 있지 않았나?


//시간복잡도 O(1)
int k;
int findk(char charX[])
{
    if(charX[0]=='-')return 0;
    int sum=0;
    for(int i=0; charX[i]; i++)
    {
        int nCases=1;
        char copied[10];
        strcpy(copied,charX);

        if(charX[i]-'0'<k) if(i!=0) copied[i-1]-=1;
        if(i==0&&charX[i]-'0'<k) continue;    
        for(int j=0; copied[j]; j++)
            if(i!=j) nCases*=((copied[j]-'0')+1);
        sum+=nCases;
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

