#include<stdio.h>
int d[10010][5], data[5], X, a[5] = { 0,1,5,10,25 };
int main()
{
    int i, j, k, l;
    scanf("%d", &X);
    for (i = 1; i <= 4; i++)
    {
        scanf("%d", &data[i]);
    }
    for (i = 1; i <= 4; i++)
    {
        for (j = X; j >= 0; j--)
        {
            if (d[j][0] != 0 || j == 0)
            {
                for (k = 1; k <= data[i]; k++)
                { // a[i]: 동전단위, k: 개수 , d[j][0]=j원만드는 데 사용한 동전개수
                    if (j + a[i] * k <= X   &&   d[j][0] + k > d[j + a[i] * k][0])
                    {
                        d[j + a[i] * k][0] = d[j][0] + k;
                        for (l = 1; l <= 4; l++) // 단위별 동전개수
                        {
                            d[j + a[i] * k][l] = d[j][l];
                        }
                        d[j + a[i] * k][i] = d[j][i] + k;
                    }
                }
            }
        }
    }
    printf("%d %d %d %d", d[X][1], d[X][2], d[X][3], d[X][4]);
    return 0;
}