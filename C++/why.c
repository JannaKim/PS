// funcA
#include<stdio.h>
void funcA(int * a);
int main()
{
    int b = 9;
    int c = 2;
    int *a = &b;
    funcA(a);
    //a = 4;
    printf("%p %p ,, %p", &c, a, &b); 
    return 0;
}
void funcA(int * a)
{
    //a = 4;
    printf("%d ",*a);
    return;
}
/*
int main()
{
    int a=1;
    int b=2;
    funcA(&a, &b); // 100, 104
    //a = 4;
    printf("%d %d", a, b); 
    return 0;
}
void funcA(int * a, int *b)
{
    int tmp = *a;
    *a = *b;
    *b = tmp;
}
*/