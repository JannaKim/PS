
#include <stdio.h>
#include <vector>
#include <iomanip>
#include <iostream>
using namespace std;
int main()
{
    vector<double> ans;
    int C;
    scanf("%d",&C);
    for(int t=0;t<C;t++)
    {
        int N;
        vector<double> score;
        scanf("%d",&N);
        int x;
        int sum=0;
        for(int i=0;i<N;i++) //input
        {
            scanf("%d",&x);
            score.push_back(x);
            sum+=x;
        }

        typedef vector<double>::size_type vsz;
        vsz size = score.size();
        cout<<size<<endl;
        int av=1.f*sum/N;
        int cnt=0;
        for(int i=0;i<N;i++)
        {
            if(score[i]>av) cnt++;
        }
        ans.push_back(1.f*cnt/N*100);

    }
    for(int i=0;i<C;i++)
    {
        printf("%.3lf%%\n",ans[i]); //% 기호 자체 출력: 2개 중복해줘야 한다.
        
    }
    
    //cout<<ans.begin()<<' '<<ans.end()<<endl;
    //printf("%d %d",ans.begin(), ans.end());
    printf("%lf,%lf",ans.front(),ans.back());

    cout<<'\n';
    for(int i=0;i<ans.size();i++)
    {
        cout<<ans[i]<<" ";
    }
    
    sort(ans.begin(),ans.end());

    for(vector<int>::iterator i= ans.begin(); i!=ans.end();i++)
    {
        cout<<*i<<" ";
    }

    for(auto ir= ans.rbegin(); ir!=ans.rend(); ++ir) // 뒤에서부터 출력
    { // ans.rend()포함 안하고 돌리나?
        cout<<*ir<<" ";
    }

    return 0;
}