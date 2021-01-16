#include <stdio.h>
#include <iostream>
using namespace std;
int n, r, c;
int z(int y, int x, int n);

int twopow(int n){
    int ans=1;
    for(int i=1;i<=n; ++i)
    {
        ans*=2;
    }
    return ans;
}

int main()
{
    
    scanf("%d %d %d", &n, &r, &c);
    printf("%d", z(0,0,twopow(n)));

}

int z(int y, int x, int n)
{
    if(n==1) return 0;
    int half= n>>1;
    int piece= half*half;
    if(r<y+half){
        if(c<x+half){ // upleft
            return z(y,x,half);
        }
        else{//upright
            return piece+z(y,x+half,half);
        }
    }
    else{
        if(c<x+half){ // downleft
            return 2*piece+ z(y+half,x,half);
        }
        else{//downright
            return 3*piece+ z(y+half,x+half,half);
        }
    }
}