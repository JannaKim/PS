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
    int num=1;
    priority_queue<pair<int, int>, vector<pair<int, int>>,greater<pair<int, int>>> pq_remain;
    while(1)
    {
        int end=0;
        // use it
        pq_remain = priority_queue <pair<int, int>, vector<pair<int, int>>,greater<pair<int, int>>>(); // reset it
        while(!pq.empty())
        {
            if(pq.top().first>=end) end=pq.top().second;
            else pq_remain.push(make_pair(pq.top().first, pq.top().second));
            pq.pop();
        }

        if(pq_remain.empty()) break;
        else { ++num; pq=pq_remain; }
    }
    printf("%d",num);

}