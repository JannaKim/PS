#include <stdio.h>
#include <string.h>

int main()
{

    int n;
    scanf("%d\n",&n);


    int hash[5000+1];
    memset(hash,0,sizeof(hash));
    int mode=-1;
    int mostFrequentN=-1;
    for(int i=0;i<n;i++)
    {
        int x;
        scanf("%d",&x);
        hash[x]+=1;
        if(mode<hash[x])
        {
            mode= hash[x];
            mostFrequentN= x;
        }
    }

    printf("최빈값: %d, 최빈수: %d",mode, mostFrequentN);

}