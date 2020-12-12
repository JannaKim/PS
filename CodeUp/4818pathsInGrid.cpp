#include <stdio.h>
#include <string.h>
int main(){
    int h, w, o;
    scanf("%d %d %d", &h, &w, &o);


    int x, y;
    y = (o-1)/w;
    y+=1;
    x = (o-1)%w; //이거 정리하기
    x+=1;
    //printf("%d %d\n",y,x);

    
    //int grid[h][w] = {0, };
    int grid[(h+1)][(w+1)];
    memset(grid,0,sizeof(grid));
    grid[1][1]=1;
/*
    for(int i=0;i<=h;i++)
    {
        for(int j=0;j<=w;j++)
        {
            printf("(%d,%d)%d ",i,j,grid[i][j]);
        }
        printf("\n");
    }
    */

    //cal

    for(int i=1;i<=y;i++)
    {
        for(int j=1;j<=x;j++)
        {
            if(i==1&j==1) continue;
            grid[i][j] = grid[i-1][j]+grid[i][j-1];
            //printf("%d %d %d\n",i,j,grid[i][j]);
            
        }
    }

    for(int i=y;i<=h;i++)
    {
        for(int j=x;j<=w;j++)
        {
            grid[i][j] = grid[i-1][j]+grid[i][j-1];
            //printf("%d %d %d\n",i,j,grid[i][j]);
        }
    }
    
/*
    for(int i=0;i<h;i++)
    {
        for(int j=0;j<w;j++)
        {
            printf("(%d,%d)%d ",i,j,grid[i][j]);
        }
        printf("\n");
    }
*/



    printf("%d\n",grid[h][w]);






}