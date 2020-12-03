
#include <stdio.h>
#include <vector>
#include <iomanip>
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
    
    return 0;
}