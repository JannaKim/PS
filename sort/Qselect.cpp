#include <stdio.h>
#include <iostream>
#include <string.h>
#include <cstdlib>
using namespace std;
#define FOR(i,n) for(int i=0;i<n;++i)
// 1 2 7 3 8 9
int A[5000000+1];

void swap(int *a, int *b){
    int tmp= *a;
    *a= *b;
    *b=tmp;
}

    
int main()
{
    int n, k;
    scanf("%d %d",&n,&k);

    FOR(i,n)
        scanf("%d",&A[i]);
    
    int start=0;
    int end= n-1;
    int i;
    int j;
    int p;
    while(start<end)
    {
        i= start+1;
        j= end;
        int here= rand()%(end-start+1)+start;
        //cout<<start<<' '<<here<<' '<<end<<' '<<'\n';
        //for(int i=0; i<=n-1;++i) cout<<A[i]<<' ';
        swap(&A[here], &A[start]);
        //for(int i=0; i<=n-1;++i) cout<<A[i]<<' ';
        p= A[start];
        while(i<=j)
        {
            while(i<=end && A[i]<=p){
                ++i;
            } 
            while(A[j]>p) --j;
            if(i<j)
                swap(&A[i], &A[j]);
        } // 1 2 7 3 8 9
        swap(&A[start], &A[j]);

        if(j-start>=k) end=j-1;
        else if(j-start+1==k) break;
        else{
            start=j+1;
            k-=j-start+1;
        }
    }
    cout<<A[j];

}

//nth_element(a.begin(), a.begin()+K, a.end());