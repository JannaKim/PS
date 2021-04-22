#include <stdio.h>
int main()
{
    long long a, b, v;
    scanf("%lld %lld %lld", &a, &b, &v);

    long long start=a;
    long long day=1;
    long long q= (v-start)/(a-b);
    day+=q;
    if(start+q*(a-b)<v) day+=1;
    printf("%lld",day);
}