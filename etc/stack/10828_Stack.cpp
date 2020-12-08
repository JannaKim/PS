#include <stdio.h>
#include <string.h>

#define MAX_SIZE 10000
#define TRUE 1
#define FALSE 0
#define EMPTY 1
#define NOT_EMPTY 0
#define NO_EL_IN_STACK -1


typedef struct _stack{
    int arr[MAX_SIZE];
    int top;
}Stack;

void StackInit(Stack *sp){
    sp->top= -1;
}

int Full(Stack *sp){
    if(sp->top+1>=MAX_SIZE) return TRUE;
    return FALSE;
}
void Push(Stack *sp, int el){
    if(Full(sp)==TRUE) return;
    sp->arr[++(sp->top)]=el;
}

int Empty(Stack *sp){
    if(sp->top== -1) return EMPTY;
    return NOT_EMPTY;
}

int Pop(Stack *sp){
    if(Empty(sp)==EMPTY) return NO_EL_IN_STACK;
    return sp->arr[(sp->top)--];
}

int Size(Stack *sp){
    return sp->top+1;
}

int Top(Stack *sp){
    if(Empty(sp)) return NO_EL_IN_STACK;
    return sp->arr[sp->top];
}


int main()
{
    Stack stack;
    StackInit(&stack);

    int numOfCommand;
    scanf("%d",&numOfCommand);
    fgetc(stdin); // 버퍼 비우기

    char command[5+1];
    
    for(int i=0;i<numOfCommand;i++)
    {
        scanf("%s",command);
        fgetc(stdin);

        if(!strcmp(command,"push"))
        {
            int element;
            scanf("%d\n",&element);
            Push(&stack, element);
        }

        else if(!strcmp(command,"pop"))
            printf("%d\n", Pop(&stack));

        else if(!strcmp(command,"size"))
            printf("%d\n", Size(&stack));
        
        else if(!strcmp(command,"empty"))
            printf("%d\n", Empty(&stack));
        else if(!strcmp(command,"top"))
            printf("%d\n", Top(&stack));
    }

    return 0;


}