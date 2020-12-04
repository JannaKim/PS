//현재 자리수만 1이고 나머지가 0인 mask과 input 값과 & 연산(and 연산)을 하면 현재 자리수의 값이 0인지 1인지 알 수가 있습니다.

#include<iostream>
#include<stdio.h>
int main()
{
    int mask;
    for(int i=5;i>-1;i--)
    {
        mask = 1<<i;
        //printf("%d\n",mask);
        printf("%d",8&mask?1:0);

        
    }
    return 0;
}
