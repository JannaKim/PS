#include <stdio.h>
using namespace std;
#define FOR(i,n) for(int i=0;i<n;++i)
void QS(int start, int end);
int ls[1000+1];

int main()
{
    int n;
    scanf("%d",&n);
    FOR(i,n){
        int x;
        scanf("%d", &x);
        ls[i]=x;
    }
    QS(0,n-1);
    FOR(i,n) printf("%d\n",ls[i]);
}

void swap(int* a, int* b)
{
    int tmp= *a;
    *a= *b;
    *b=tmp;
}

/*
inline void swap(int &i, int &j)
{
    int temp= i;
    i= j;
    j= temp;
}

inline void swap(double &i, double &j)
{
    double temp= i;
    i= j;
    j= temp;
}
*/
void QS(int a, int b)
{
    if(a>=b) return;
    int start =a;
    int end= b;
    int p= ls[(start+end)>>1];
    while(start<=end)
    {
        while(ls[start]<p) ++start;
        while(ls[end]>p) --end;
        if(start<=end){
            if(ls[start]>ls[end])
                swap(&ls[start],&ls[end]);
            ++start;
            --end;
        }
    }
    QS(a, end);
    QS(start, b);
}