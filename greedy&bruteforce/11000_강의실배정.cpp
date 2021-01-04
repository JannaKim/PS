#include <iostream>
#include <vector>
#include <algorithm>
#include <stdio.h>
#include <functional>
#include <queue> //여기에 뭘 넣을지 생각하ㅣㄱ
using namespace std;

int sch[200000+1][3];

int main()
{
    int n;
    scanf("%d\n",&n);
    vector<pair<int, int>> lec;
    for(int i=0;i<n;++i)
    {
        int a, b;
        scanf("%d %d",&a, &b);
        lec.push_back({a,b});

    }
    sort(lec.begin(), lec.end());
    priority_queue<int> pq;
    int end=0;
    for(auto el: lec){
        if end<=el[0]

    }

    /*
    cnt=1
    sort하고
    끝시간<=시작시간이면 contin
    아니면 pq 에 넣음
    남은 거 있으면 다시 포문 cnt++
    */

}