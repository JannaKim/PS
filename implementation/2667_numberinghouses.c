#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

void process();
bool possi();
int n;
int **a;
int **chk;
int main()
{
    
    scanf("%d",&n);
    a = (int **)malloc(n * sizeof(int *));
    chk = (int **)malloc(n * sizeof(int *));
    for(int i=0;i<n;++i)
    {
        a[i] = (int *)malloc(n * sizeof(int));
        chk[i] = (int *)calloc(n , n * sizeof(int));
    }
    for(int i = 0; i<n ; ++i)
    {
        for(int j=0; j< n ; ++j)
        {
            scanf("%d" , &a[i][j]);
        }
    }

    process();

}

void process()
{
    for(int i=0; i<n ; ++i)
    {
        for(int j=0; j<n; ++j)
        {
            if(possi(i,j)) bfs(i , j);

        }
    }
}

bool possi(y , x)
{
    if(chk[y][x] == 0 && a[y][x] ==1) return true;
    return false;
}