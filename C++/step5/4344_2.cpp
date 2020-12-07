
#include <stdio.h>
#include <vector>
#include <iomanip>
#include <iostream>
#include <algorithm>
using namespace std;
int main()
{
    vector<double> ans;
    vector<double> sc_list;
    int C;
    scanf("%d",&C);
    for(int t=0;t<C;t++)
    {
        int N;
        vector<double> scores;
        scanf("%d",&N);
        int x;
        int sum=0;
        for(int i=0;i<N;i++) //input
        {
            scanf("%d",&x);
            scores.push_back(x);
            sum+=x;
        }

        typedef vector<double>::size_type vsz;
        vsz sc_size = scores.size();
        cout<<sc_size<<endl;
        int av=1.f*sum/N;
        int cnt=0;

        
        /*
        for(int i=0;i<N;i++)
        {
            if(scores[i]>av) cnt++;
        }
        */
       cnt=0;
       for(const auto &sc: scores)
       {
           if(sc>av) cnt++;
       }


        /*
        vector<double> sc_list;
        copy_if(score.begin(), score.end(), back_inserter(sc_list)),
        []
        */
        
        for(const auto & sc : scores) // for el in L
        {
        if(sc > av) sc_list.push_back(sc);
        }
        ans.push_back(1.f*cnt/N*100);

/*
    std::copy_if(all_items.begin(), all_items.end(), std::back_inserter(filter_items),
             [&bad_ids](const mystruct& item)
{
     return std::find(bad_ids.begin(), bad_ids.end(), item.id) == bad_ids.end();
});
*/


    }
    for(int i=0;i<C;i++)
    {
        printf("%.3lf%%\n",ans[i]); //% 기호 자체 출력: 2개 중복해줘야 한다.
        
    }

    //sc_list 출력
    for(int i=0;i<sc_list.size();i++) cout<<sc_list[i]<<"\n";
    


    //cout<<ans.begin()<<' '<<ans.end()<<endl;
    //printf("%d %d",ans.begin(), ans.end());
    printf("%lf,%lf",ans.front(),ans.back());

    cout<<'\n';
    for(int i=0;i<ans.size();i++)
    {
        cout<<ans[i]<<" ";
    }
    
    sort(ans.begin(),ans.end());
    cout<<'\n';
    for(auto it = ans.begin(); it!=ans.end();it++) 
    {
        cout<<*it<<" ";
    }

    //reverse(ans.begin(),ans.end());
    cout<<'\n';
    for(auto it=ans.rbegin(); it!=ans.rend(); ++it) // 뒤에서부터 출력
    { // ans.rend()포함 안하고 돌리나?
        cout<<*it<<" ";
    }

    return 0;
}

