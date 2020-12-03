#include <iostream>
#include <string>

#include <iomanip>
#include <ios>
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


    // cout.setf(ios::fixed);

    //cout<<A*10/B<<endl;


    //총 세 자리로 출력하기

    /*

    endl 느리다: 줄바꿈을 출력하고 flush하는것까지 포함하기 때문.


    출력속도는 cin cout이 scanf, printf 보다 느리다.

    ios_base::sync_with_stdio(false); //하면 매우빨라지지만 printf와 섞어서 쓸 수 없다
    */

    streamsize prec = cout.precision();
    cout<<3.14159265<<'\n' // 3.14159265
    <<setprecision(3)<<3.14159265<<'\n' //3.14
    <<setprecision(prec)<<3.14159265<<'\n' //3.14159265
    <<fixed<<setprecision(9)<<3.14159265<<'\n' //3.141592650
    <<setprecision(prec)<<3.141592653589 <<'\n'//3.141593
    <<fixed<<setprecision(4)<<3.14159265<<'\n' //3.1416
    <<setprecision(prec)<<3.141592653589 <<'\n';//3.141593


    /*
    string s;
    getline(cin,s);

    cout<<s<<endl;
    */


}