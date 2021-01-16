#include <stdio.h>
#include <algorithm>
#include <vector>
using namespace std;

void fill(int queen);
void backtracking(int floor, int num);
void chessboard(int board);
int n;
int check[230];
int ans=0;

int main()
{
    scanf("%d",&n);
    backtracking(0,1);
    printf("%d",ans);
}

void backtracking(int floor, int num)
{
    //printf("num: %d\n",num);
    if(floor==n) return;
    int prv[230];
    for(int i=0;i<230;++i) prv[i]=check[i];
    for(int i=0;i<n;++i)
    {
        int play=n*floor+i;
        if(!check[play]){
            if(num==n)ans+=1;
            check[play]=1;
            //chessboard(bitmask);
            fill(n*floor+i);
            backtracking(floor+1,num+1);
            for(int i=0;i<230;++i) check[i]=prv[i];
        }

    }
    backtracking(floor+1,num);
}

void fill(int queen)
{
     //d
    for(int i=1;i<n;++i)
    {
        if(queen+n*i>=n*n) break;
        check[queen+n*i]=1;
    }
    //dr
    for(int i=1;i<n;++i)
    {
        if((queen+n*i+i)/n > queen/n+i) break;
        if(queen+n*i<n*n) check[queen+n*i+i]=1;
        else break;
    }
    //dl
    for(int i=1;i<n;++i)
    {
        if((queen+n*i-i)/n < queen/n+i) break;
        check[queen+n*i-i]=1;      
    }

}
/*
void chessboard(int board)
{
    for(int i=0; i<n*n; ++i)
    {
        int mask=1<<i;
        ((board&mask)?printf("1"):printf("0"));
        if((i%n)==n-1) printf("\n");
    }
    printf("\n");
}
*/