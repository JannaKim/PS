#include <iostream>
#include <queue>

using namespace std;

int main(void)
{
    int n, m;
    cin>>n;
    cin>>m;
    priority_queue<long long, vector<long long>,greater<long long>> pq;
    while(n--){
        long long x;
        cin>>x;
        pq.push(x);
    }
    while(m--)
    {
        long long temp= pq.top();
        pq.pop();
        temp+= pq.top();
        pq.pop();
        pq.push(temp);
        pq.push(temp);
    }
    long long sum=0;
    for(; !pq.empty(); pq.pop())
        sum+=pq.top();
    cout<<sum;

}

/*
#include <algorithm>
#include <stdio.h>
#include <vector>
using namespace std;
int main()
{
    int n, m;
    scanf("%d %d\n",&n, &m);
    vector<long long int> cards;
    while(n--){
        int x;
        scanf("%d",&x);
        cards.push_back(x);
    }
    while(m--){
        sort(cards.begin(), cards.end());
        
        //long long int *x= &cards[0];
        //long long int *y= &cards[1];
        //while(*x==*y) ++y;

        //*x= *x+*y; //unite smallest 2 cards
        //*y= *x;
        
       cards[0]+=cards[1];
       cards[1]=cards[0];
    }
    long long int sum=0;
    for(auto & n: cards) sum+=n;
    printf("%lld",sum);
}
*/