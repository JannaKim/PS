#include <stdio.h>
#include <string>
#include <cstring>
#include <iostream>
using namespace std;


class Queue{
    private:
    
    
    public:
        int queue[10000+1];
        int top;
        int bottom;
        Queue(){
            top=0;
            bottom=0;
        }

        void push(int number)
        {
            queue[top++]=number;
        }

        int pop()
        {
            if(top==bottom){
                return -1;
            }
            if(top!=bottom)
                return queue[bottom++];
        }       

        int size()
        {
            return top-bottom;
        }

        int isEmpty()
        {
            if(top-bottom==0)
            {
                return 1;
            }
            return 0;
        }

        int front()
        {
            if(top-bottom==0)
            {
                return -1;
            }
            return queue[bottom];
        }

        int back()
        {
            if(top-bottom==0)
            {
                return -1;
            }
            return queue[top-1];
        }

};


int main()
{
    Queue* myQueue = new Queue();
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
            myQueue->push(number);
        }

        else if(!strcmp(command,"pop"))
        {
            cout<<myQueue->pop()<<'\n';
        }

        else if(!strcmp(command,"size"))
        {
            cout<<myQueue->size()<<'\n';
        }
        else if(!strcmp(command,"empty"))
        {
            cout<<myQueue->isEmpty()<<'\n';
        }

        else if(!strcmp(command,"front"))
        {
            cout<<myQueue->front()<<'\n';
        }

        else if(!strcmp(command,"back"))
        {
            cout<<myQueue->back()<<'\n';
        }

    }


}