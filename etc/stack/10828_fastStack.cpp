#include <cstdio>
#include <cstring>
#define MAX_SIZE 10000


int main()

{
    int myStack[MAX_SIZE+1];
    int top=-1;

    int nmOfCmd;
    scanf("%d",&nmOfCmd);

    char curCmd[5+1];
    while(nmOfCmd--)
    {
        
        scanf("%s", curCmd); //scanf string은 그냥 받네
        if(!strcmp(curCmd,"push"))
        {
            scanf("%d",myStack+ ++top);
            if(top>=MAX_SIZE) --top;
        }

        else if(!strcmp(curCmd,"pop"))
        {
            if(top==-1) printf("-1\n");
            else printf("%d\n", myStack[top--]);
        }

        else if(!strcmp(curCmd,"top"))
        {
            if(top==-1) printf("-1\n");
            else printf("%d\n",myStack[top]);
        }

        else if(!strcmp(curCmd,"empty"))
            printf("%d\n",top==-1? 1:0);
        else if(!strcmp(curCmd,"size"))
            printf("%d\n",top+1);

    }
    return 0;


}