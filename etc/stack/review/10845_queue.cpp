#include <stdio.h>
#include <cstring>
#include <string>
#include <string.h>
#include <iostream>
using namespace std;



class Queue{
private:
    int queue[10000+1];
    memset(queue,0,sizeof(queue)); //?
    int top=0;
    int bottom=0;

public:
    Queue(){}

    void push(int num)
    {
        if(top-bottom>=10000) return;
        queue[top++]=num;
    }

    int pop(){
        if(top==bottom) return -1;
        return queue[bottom++];
    }

    int size()
    {
        return top-bottom;
    }

    int empty()
    {
        if(top==bottom) return 1;
        return 0;
    }

    int front()
    {
        if(top==bottom) return -1; 
        return queue[bottom];
    }

    int back()
    {
        if(top==bottom) return -1; 
        return queue[top-1]; //        
    }
};


int main()
{
    int n;
    scanf("%d\n",&n);
    //Queue* myQueue = new Queue();
    Queue myQueue;

    while(n--)
    {
        char command[5+1];
        scanf("%s",command);

        
        if(!strcmp(command,"push"))
        {
            int num;
            scanf("%d",&num);
            myQueue.push(num);
        }

        else if(!strcmp(command,"pop"))
        {
            printf("%d\n",myQueue.pop());
        }

        else if(!strcmp(command,"size"))
        {
            printf("%d\n",myQueue.size());
        }
        else if(!strcmp(command,"empty"))
        {
            printf("%d\n",myQueue.empty());
        }
        else if(!strcmp(command,"front"))
        {
            printf("%d\n",myQueue.front());
        }
        else if(!strcmp(command,"back"))
        {
            printf("%d\n",myQueue.back());
        }
    }
}