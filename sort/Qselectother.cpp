#include <stdio.h>
#include <cstdlib>
using namespace std;
#define FOR(i,n) for(int i=0;i<n;++i)
// 1 2 7 3 8 9
int A[5000000+1];


    
int main()
{
    int n, k;
    scanf("%d %d",&n,&k);

    FOR(i,n)
        scanf("%d",&A[i]);
    
    int start=0;
    int end= n-1;
    int p;
    int ans;
    while(start<end)
    {
        int i= start-1;
        int j= end;
        int here= rand()%(end-start+1)+start;
        //cout<<start<<' '<<here<<' '<<end<<' '<<'\n';
        //for(int i=0; i<=n-1;++i) cout<<A[i]<<' ';
        int tmp= A[here];
        A[here]= A[end];
        A[end]= tmp;

        //for(int i=0; i<=n-1;++i) cout<<A[i]<<' ';
        p= A[end];
        while(i<j)
        {
            while(A[++i]<p);
            while(j>start && A[--j]>p);
            if(i<j){
                tmp= A[i];
                A[i]= A[j];
                A[j]= tmp;
            }
        } // 1 2 7 3 8 9
        tmp= A[i];
        A[i]= A[end];
        A[end]= tmp;
        if(i>=k) end=i-1;
        else if(i<k-1) start=i+1;
        else{
            ans=A[i];
        }
    }
    if(start==end && start==k-1) ans=A[start];
    printf("%d",ans);

}

//nth_element(a.begin(), a.begin()+K, a.end());