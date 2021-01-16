#include <vector>
#include <stdio.h>
#include <queue>
#include <utility>
using namespace std;

int main()
{
    int n;
    scanf("%d\n",&n);

    priority_queue<pair<int, int>, vector<pair<int, int>>,greater<pair<int, int>>> pq;
    
    for(int i=0;i<n;++i)
    {
        int a, b;
        scanf("%d %d",&a, &b);
        pq.push(make_pair(a,b));

    }
    priority_queue<int, vector<int>,greater<int>> room;
    room.push(0);
    while(!pq.empty())
    {
        auto[start, end]= pq.top();
        pq.pop();
        if(start>=room.top()) {room.pop(); room.push(end);}
        else room.push(end);
    }
    printf("%d",room.size());

}