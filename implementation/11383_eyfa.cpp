#include <iostream>
#include <cstring>
#include <stdio.h>
#include <string.h>
using namespace std;
int main()
{
    char a[21][21];
    int N, M;
    cin>>N;
    cin>>M;
    for(int k=0;k<2*N;k++)
        scanf("%s",a[k]);
        

    for(int i=N; i<2*N;++i)
    {
        for(int j=0; j<2*M;++j)
        {
            //cout<<i<<" "<<j<<" \n";
            //cout<<a[i%N][j>>1]<<" "<<a[i][j]<<"\n";
            if(a[i%N][j>>1]!=a[i][j])
            {
                cout<<"Not Eyfa\n";
                return 0;
            }
        }
    }
    cout<<"Eyfa\n" ;
    return 0;
}
