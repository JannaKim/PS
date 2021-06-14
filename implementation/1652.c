#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

int main()
{
    int n;
    scanf("%d\n", &n);
    char **a = (char **)malloc(n * sizeof(char*));
    for(int i = 0; i < n; ++i)
    {
        a[i] = (char *)malloc(n * sizeof(char));
    }
    for(int i = 0; i < n; ++i)
    {
        for(int j = 0; j < n; ++j)
        {
            scanf("%c",&a[i][j]);
        }
        char tmp;
        scanf("%c" , &tmp);
    }
    
    
    int ans = 0;

    for(int i = 0; i < n; ++i)
    {
        bool flag = false;
        for(int j = 0; j < n - 1; ++j)
        {
            if(a[i][j]=='.' && a[i][j+1]=='.')
            {
                if(flag == false)
                {
                    flag = true;
                    ans++;
                }
            }
            else
            {
                flag=false;
            }
            
        }
    }
    printf("%d " , ans);

    char **b = (char **)malloc(n * sizeof(char*));
    for(int i = 0; i < n; ++i)
    {
        b[i] = (char *)malloc(n * sizeof(char *));
    }

    for(int i= 0; i < n ; ++i)
    {
        for(int j = 0; j < n; ++j)
        {
            //b[i][j] = a[j][n-i-1];
            strncpy( &(*(b+i))[j], &(*(a+j))[n-i-1], sizeof(char));
        }
    }

    ans = 0;

    for(int i = 0; i < n; ++i)
    {
        bool flag = false;
        for(int j = 0; j < n - 1; ++j)
        {
            if(b[i][j]=='.' && b[i][j+1]=='.')
            {
                if(flag == false)
                {
                    flag = true;
                    ans++;
                }
            }
            else
            {
                flag=false;
            }        
        }
    }

    printf("%d" , ans);

    for (int i = 0; i < n; i++) 
        free(a[i]); 
    free(a);

    for (int i = 0; i < n; i++) 
        free(b[i]); 
    free(b);
    
}