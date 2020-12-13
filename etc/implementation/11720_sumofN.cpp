#include <string.h>
#include <stdio.h>
using namespace std;

int main()
{
    int n;
    scanf("%d\n",&n);
    char input[100+1];
    scanf("%s",input);
    int sum=0;
    for(int i=0;input[i];i++)
        sum+= input[i]-'0';
    printf("%d\n",sum);
}

/*
char inArr[101] = {0, };
scanf_s("%s", inArr, 101);
*/