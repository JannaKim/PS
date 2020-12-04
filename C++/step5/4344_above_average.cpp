#include <iostream>
#include <iomanip>
#include <vector>
using namespace std;


int main(){
    ios_base::sync_with_stdio(false);
    int C;
    cin>>C;
    cout<<fixed<<setprecision(3);
    for(int t=0;t<C;t++)
    {
        int N;
        cin>>N;
        vector<double> score;
        double x;
        double sum=0;
        for(int i=0;i<N;i++)
        {
            cin>>x;
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
        cout<<ans*100<<"%"<<'\n';


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

//getchar 버퍼에서 가장 앞에 대기하고 있는 하나를 가져오는 것
