#include <stdio.h>
#include <string>
#include <cstring>
using namespace std;

int main(){
    int queue[10000+1];
    int top= 0; //top 0이면 어떤 경우라도 비어있음
    int bottom= 0; //queue[0] 비어있을때도 0, 차 있을때도 0 

    int n;
    scanf("%d\n",&n);
    while(n--)
    {
        char command[5+1];
        scanf("%s",command);

        if(!strcmp(command,"push"))
        {
            int number;
            scanf("%d",&number);
            if(top-bottom >= 10000) continue;
            queue[top++]=number;
        }

        else if(!strcmp(command,"pop"))
        {
            if(top==0){
                printf("-1"); 
                continue;
            }
            if(top!=bottom)
                printf("%d\n",queue[bottom++]);
            else
                printf("-1");
        }

        else if(!strcmp(command,"size"))
        {
            printf("%d\n",top-bottom);
        }
        else if(!strcmp(command,"empty"))
        {
            if(top-bottom==0)
            {
                printf("%d\n",1);
                continue;
            }
            printf("%d\n",0);
        }

        else if(!strcmp(command,"front"))
        {
            if(top-bottom==0)
            {
                printf("%d\n",-1);
                continue;
            }
            printf("%d\n",queue[bottom]);
        }

        else if(!strcmp(command,"back"))
        {
            if(top-bottom==0)
            {
                printf("%d\n",-1);
                continue;
            }
            printf("%d\n",queue[top-1]);
        }

    }

}