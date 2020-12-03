#include <iostream>
using namespace std;
int main()
{
    double A, B;
    cin>>A;
    cin>>B;
    //cout<<A/B<<endl;
    //printf("%.9f\n",A/B);
    //printf: 실수, 소수자리수를 각각 지정할 수 있다
    //cout: 실수와 소수를 초함한 자리수를 지정한다
    cout<<fixed; // 소수점을 고정시켜 표현
    cout.precision(9);
    cout<<A/B<<endl;
    cout.unsetf(ios::fixed);
    //cout<<A*10/B<<endl;



}