#include <stdio.h>
#include <algorithm>
using namespace std;
int main()
{
    int n;
    scanf("%d\n",&n);
    int a, b, c;
    scanf("%d %d %d", &a, &b, &c);

    int left[3]= {a,a,}, mid[3]={b,b,}, right[3]={c,c,}; //{max, min, }

    
    int Lmax, Lmin, Mmax, Mmin, Rmax, Rmin;
    while(--n)
    {
        scanf("%d %d %d", &a, &b, &c);
        Lmax= a+ max(left[0], mid[0]);
        Lmin= a+ min(left[1], mid[1]);

        Mmax= b+ max({left[0], mid[0], right[0]});
        Mmin= b+ min({left[1], mid[1], right[1]});

        Rmax= c+ max(mid[0], right[0]);
        Rmin= c+ min(mid[1], right[1]);

        //left[0], left[1], mid[0], mid[1], right[0], right[1]= Lmax, Lmin, Mmax, Mmin, Rmax, Rmin;
        left[0]= Lmax;
        left[1]= Lmin;
        mid[0]= Mmax;
        mid[1]= Mmin;
        right[0]= Rmax;
        right[1]= Rmin;
        //printf("%d %d %d %d %d %d\n", left[0], left[1], mid[0], mid[1], right[0], right[1]);
    }

    printf("%d %d\n", max({left[0], mid[0] ,right[0]}), min({left[1], mid[1] ,right[1]}));

}