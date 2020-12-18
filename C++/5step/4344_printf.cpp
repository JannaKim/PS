#include <iostream>
#include <iomanip>
#include <vector>
using namespace std;
#include <stdio.h>


int main(){
/*
    int N;
    cin>>N;
    for(int i=0;i<N;i++)
    {
        int n;
        cin>>n;
        cout<<"*"<<n<<'\n';

    }
*/

/*
30
1
2
3
4
5
6
7
8
9
10
1
2
3
4
5
6
7
8
9
10
1
2
3
4
5
6
7
8
9
10
*/

    //ios_base::sync_with_stdio(false);
    
    int C;
    scanf("%d",&C);
    for(int t=0;t<C;t++)
    {
        int N;
        scanf("%d",&N);
        vector<double> score;
        double x;
        double sum=0;
        for(int i=0;i<N;i++)
        {
            scanf("%d",&x);
            score.push_back(x);
            sum+=x;
        }
        double av = sum/N;
        double cnt=0;
        for(int i=0;i<N;i++)
        {  
            if(score[i]>av) cnt++;
        }
        //cout<<av<<" "<<cnt<<" "<<N<<endl;
        double ans=cnt/N; // int / double = 0?
        // 애초에 int로 나누는데 앞에 1.f붙여주면 될듯.
        printf("%.3lf%\n",ans*100);

    }
    
    return 0;
}
/*
5
5 50 50 70 80 100
7 100 95 90 80 70 60 50
3 70 90 80
3 70 90 81
9 100 99 98 97 96 95 94 93 91
*/
