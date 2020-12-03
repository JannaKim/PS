#include <iostream>
#include <iomanip>
#include <vector>
using namespace std;

int main(){
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
3 70 90 805 50 50 70 80 100
*/