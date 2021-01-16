#include <stdio.h>
#include <algorithm>
#include <vector>
using namespace std;

void fill(int queen);
void backtracking(int floor, int num);
void chessboard(int board);
int n;
int bitmask=0;
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
    if(floor==n) {return;}
    int prv= bitmask;
    for(int i=0;i<n;++i)
    {
        int play= 1<<(n*floor+i);
        if(!(bitmask&play)){
            if(num==n)ans+=1;
            bitmask|=play;
            //chessboard(bitmask);
            fill(n*floor+i);
            backtracking(floor+1,num+1);
            bitmask=prv;
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
        int mark= 1<<(queen+n*i);
        bitmask|=mark;
    }
    //dr
    for(int i=1;i<n;++i)
    {
        if((queen+n*i+i)/n > queen/n+i) break;
        int mark= 1<<(queen+n*i+i);
        bitmask|=mark;        
    }
    //dl
    for(int i=1;i<n;++i)
    {
        if((queen+n*i-i)/n < queen/n+i) break;
        int mark= 1<<(queen+n*i-i);
        bitmask|=mark;        
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